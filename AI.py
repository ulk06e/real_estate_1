import time
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url="https://api.proxyapi.ru/openai/v1")

def get_response(model, messages):
    stream = client.chat.completions.create(
            model=model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in messages
            ],
            stream=True,
        )
    return stream