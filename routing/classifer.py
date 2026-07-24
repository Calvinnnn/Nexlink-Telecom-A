from openai import OpenAI
from prompts import CLASSIFICATION_PROMPT

client = OpenAI()

def classify(customer):

    prompt = f"""
{CLASSIFICATION_PROMPT}

Customer:
{customer}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()