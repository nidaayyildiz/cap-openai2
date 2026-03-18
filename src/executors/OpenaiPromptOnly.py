"""
OpenAI Executor: Sends a text-only prompt to the OpenAI API and returns the response.
"""

import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.base.capsule import Capsule
from sdks.novavision.src.helper.executor import Executor
from capsules.Openai.src.utils.response import build_prompt_only_response
from capsules.Openai.src.models.PackageModel import PackageModel

import openai


class OpenaiPromptOnly(Capsule):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))

        self.prompt = self.request.get_param("ConfigPrompt")
        self.api_key = self.request.get_param("ApiKey")
        self.model_version = self.request.get_param("ModelVersion")
        self.temperature = self.request.get_param("Temperature")
        self.max_tokens = self.request.get_param("MaxTokens")
        self.reasoning_effort = self.request.get_param("ReasoningEffort")

        print(f"[DEBUG] api_key length: {len(self.api_key) if self.api_key else 0}")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def _build_messages(self):
        return [
            {
                "role": "user",
                "content": self.prompt or "",
            }
        ]

    def run(self):
        client = openai.OpenAI(api_key=self.api_key)

        messages = self._build_messages()

        kwargs = {
            "model": self.model_version,
            "messages": messages,
            "max_tokens": self.max_tokens or 1024,
        }

        if self.temperature is not None:
            kwargs["temperature"] = self.temperature

        if self.reasoning_effort and self.reasoning_effort != "none":
            kwargs["reasoning_effort"] = self.reasoning_effort

        try:
            response = client.chat.completions.create(**kwargs)

            print(f"[DEBUG] Response: {str(response)[:500]}")

            self.output_text = response.choices[0].message.content or ""
            self.parsed_classes = []

        except openai.APIError as e:
            print(f"[DEBUG] OpenAI API Error: {e}")
            self.output_text = f"API Error: {str(e)}"
            self.parsed_classes = []
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            self.output_text = f"Error: {str(e)}"
            self.parsed_classes = []

        return build_prompt_only_response(context=self)


if "__main__" == __name__:

    Executor(sys.argv[1]).run()
