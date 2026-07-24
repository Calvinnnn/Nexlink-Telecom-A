from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "gemini-3.5-flash"

_client = None


def configure_api():
    global _client

    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMENI_API")

        if not api_key:
            raise ValueError("Google API key not found.")

        _client = genai.Client(api_key=api_key)

    return _client


def call_model(prompt):
    client = configure_api()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text