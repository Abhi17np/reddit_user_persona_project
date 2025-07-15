import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

print("OPENROUTER_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("REDDIT_CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))
print("REDDIT_CLIENT_SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))
