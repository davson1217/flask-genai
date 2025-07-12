import requests
import json
from config import OPENROUTER_API_KEY, SITE_URL, SITE_NAME
from genai.base import ChatModel
from utils.error_codes import make_response

class OpenRouter(ChatModel):
    def generate_response(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": SITE_URL,
            "X-Title": SITE_NAME,
            "Content-Type": "application/json"
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
            data=json.dumps(payload)
        )

        print(response.json());

        return response.json()
    