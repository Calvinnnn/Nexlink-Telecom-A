from google import genai
from google.genai import types
from prompts import CLASSIFICATION_PROMPT

# The client automatically picks up your GEMINI_API_KEY environment variable
client = genai.Client()

def classify(customer):
    prompt = f"""
{CLASSIFICATION_PROMPT}

Customer:
{customer}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0
        )
    )

    return response.text.strip()