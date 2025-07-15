import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

def build_prompt(username, texts):
    intro = f"Create a user persona for Reddit user u/{username} based on the following content:\n\n"
    body = "\n\n".join(texts)
    outro = (
        "\n\nThe persona should include:\n"
        "- Name (if inferred)\n"
        "- Age range\n"
        "- Location\n"
        "- Occupation\n"
        "- Interests & hobbies\n"
        "- Frequently visited subreddits\n"
        "- Personality traits\n"
        "- Political/Social views (if any)\n"
        "- Add citation quotes from Reddit content under each point\n"
    )
    return intro + body + outro

import os
import requests

def generate_persona(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise Exception("❌ OPENROUTER_API_KEY not found. Check your .env file.")

    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://chat.openai.com",
        "X-Title": "Reddit Persona Generator"
    }

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",  # ✅ Valid model name
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"OpenRouter API failed: {response.text}")

    return response.json()["choices"][0]["message"]["content"].strip()

