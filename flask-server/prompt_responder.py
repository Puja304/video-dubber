from dotenv import load_dotenv
import os
from openai import OpenAI



load_dotenv() 
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Missing OPENROUTER_API_KEY in environment variables")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

def gpt_modified(prompt, language):
    response = client.chat.completions.create(
    model = "meta-llama/llama-3-8b-instruct",
    messages=[
            {
                "role": "system",
                "content": (
                    f"You are a {language} translation engine. "
                    f"You only respond with the translated sentence. "
                    f"You never include explanations, commentary, transliterations, or extra formatting."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    temperature=0.2,
    max_tokens=200
)

    return response.choices[0].message.content.strip()