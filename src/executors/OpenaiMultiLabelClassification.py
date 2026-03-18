"""
OpenAI Executor: Multi-label image classification using the OpenAI vision API.
"""

import os
import sys
import base64
import json
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.capsule import Capsule
from sdks.novavision.src.helper.executor import Executor
from capsules.Openai.src.utils.response import build_multi_label_classification_response
from capsules.Openai.src.models.PackageModel import PackageModel

import openai


class OpenaiMultiLabelClassification(Capsule):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))

        self.classes = self.request.get_param("ConfigClasses")
        self.api_key = self.request.get_param("ApiKey")
        self.model_version = self.request.get_param("ModelVersion")
        self.temperature = self.request.get_param("Temperature")
        self.max_tokens = self.request.get_param("MaxTokens")
        self.image_detail = self.request.get_param("ImageDetail")
        self.image_selector = self.request.get_param("inputImage")

        print(f"[DEBUG] api_key length: {len(self.api_key) if self.api_key else 0}")
        print(f"[DEBUG] classes type: {type(self.classes)}")
        print(f"[DEBUG] classes value: {self.classes}")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def _build_messages(self, base64_image):
        detail = self.image_detail if self.image_detail else "auto"
        serialised_classes = ", ".join(self.classes) if isinstance(self.classes, list) else (self.classes or "")
        system_instruction = (
            'You act as a multi-label classification model. Return only a JSON object: '
            '{"predicted_classes": [{"class": "class-name-1", "confidence": 0.9}]}. '
            "Only include classes that are visible in the image."
        )
        return [
            {
                "role": "system",
                "content": system_instruction,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": detail,
                        },
                    },
                    {
                        "type": "text",
                        "text": f"List of classes: {serialised_classes}",
                    },
                ],
            },
        ]

    def run(self):
        img = Image.get_frame(img=self.image_selector, redis_db=self.redis_db)

        success, encoded_image = cv2.imencode('.jpg', img.value)
        if not success:
            raise RuntimeError("Failed to encode image for API")

        base64_image = base64.b64encode(encoded_image).decode('utf-8')

        client = openai.OpenAI(api_key=self.api_key)
        messages = self._build_messages(base64_image)

        kwargs = {
            "model": self.model_version,
            "messages": messages,
            "max_tokens": self.max_tokens or 1024,
            "response_format": {"type": "json_object"},
        }

        if self.temperature is not None:
            kwargs["temperature"] = self.temperature

        try:
            response = client.chat.completions.create(**kwargs)

            print(f"[DEBUG] Response: {str(response)[:500]}")

            raw_text = response.choices[0].message.content or ""
            self.output_text = raw_text
            try:
                parsed = json.loads(raw_text)
                self.parsed_classes = parsed.get("predicted_classes", self.classes if self.classes else [])
            except json.JSONDecodeError:
                self.parsed_classes = self.classes if self.classes else []

        except openai.APIError as e:
            print(f"[DEBUG] OpenAI API Error: {e}")
            self.output_text = f"API Error: {str(e)}"
            self.parsed_classes = []
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            self.output_text = f"Error: {str(e)}"
            self.parsed_classes = []

        return build_multi_label_classification_response(context=self)


if "__main__" == __name__:

    Executor(sys.argv[1]).run()
