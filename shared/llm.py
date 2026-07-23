from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "gemini-flash-latest"

_client = None


def get_client():
    global _client #this mean the same var at the top of the file, not a local var
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) #instantiation
    return _client


def call_model(prompt):
    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text