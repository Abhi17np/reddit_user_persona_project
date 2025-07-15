# list_models.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENROUTER_API_KEY")

models = openai.Model.list()

for model in models['data']:
    print(model['id'])

