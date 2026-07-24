import warnings
import google.generativeai as genai
from dotenv import load_dotenv
import os

warnings.filterwarnings("ignore", category=FutureWarning, module=r"google\.generativeai")
load_dotenv()

MODEL_NAME = "gemini-2.0-flash"

_configured = False


def configure_api():
    global _configured
    if not _configured:
        api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMENI_API")
        genai.configure(api_key=api_key)
        _configured = True


def call_model(prompt):
    configure_api()
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text