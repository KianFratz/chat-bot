from collections import defaultdict

from ai.base import AIPlatform
from google import genai




class Gemini(AIPlatform):
    def __init__(self, api_key: str, system_prompt: str = None):
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = "gemini-2.5-flash-preview-05-20"

    def chat(self, prompt: str) -> str:
        if self.system_prompt:
            prompt = f"{self.system_prompt}\n\n{prompt}"
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )

        return response.text