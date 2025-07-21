import requests
import json
from config import OPENROUTER_API_KEY, SITE_URL, SITE_NAME
from genai.base import ChatModel
from utils.error_codes import make_response

class OpenRouter(ChatModel):
    def generate_response(self, prompt: str) -> str:
        hardcoded = "Bearer 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"
        generated = f"Bearer {OPENROUTER_API_KEY}"
        
        print(f"HARDCODED == GENERATED? {hardcoded == generated}")
        print(f"HARDCODED == {hardcoded}")
        print(f"GENERATED == {generated}")

        headers = {
            "Authorization": "Bearer " + OPENROUTER_API_KEY,
            "Content-Type": "application/json",
            "Accept": "*"
        }

        #openai/gpt-4o
        payload = {
            "model": "google/gemini-2.5-flash-lite-preview-06-17",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
        )

        ai_raw = response.json()

        print(ai_raw)
        print(headers)
        # print(payload)

        if (ai_raw.get("error")):
            return ai_raw
        

        return {
            "created": ai_raw.get("created"),
            "message": ai_raw["choices"][0]["message"]["content"]
        }
    