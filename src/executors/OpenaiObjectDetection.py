"""
OpenAI Executor: Object detection using the OpenAI vision API.
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
from capsules.Openai.src.utils.response import build_object_detection_response
from capsules.Openai.src.models.PackageModel import PackageModel

import openai


class OpenaiObjectDetection(Capsule):
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
        print(f"[DEBUG] classes: {self.classes}")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def _build_messages(self, base64_image):
        detail = self.image_detail if self.image_detail else "high"
        serialised_classes = ", ".join(self.classes) if isinstance(self.classes, list) else (self.classes or "")
        system_instruction = (
            'You act as an object-detection model. Return only a JSON object: '
            '{"detections": [{"x_min": 0.1, "y_min": 0.2, "x_max": 0.3, "y_max": 0.4, '
            '"class_name": "my-class", "confidence": 0.7}]}. '
            "All coordinates must be 0.0-1.0 as a proportion of image dimensions."
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
                self.parsed_classes = parsed.get("detections", self.classes if self.classes else [])
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

        return build_object_detection_response(context=self)


if "__main__" == __name__:

    Executor(sys.argv[1]).run()
