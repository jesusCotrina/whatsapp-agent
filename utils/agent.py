import os
from openai import OpenAI
import requests

client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

def ask_llama(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="meta-llama-3-8b-instruct",
            messages=[
                {"role": "system", "content": "Eres un asistente útil y claro."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Ocurrió un error con la IA: {str(e)}"


def download_media(media_url: str):
    response = requests.get(
        media_url,
        auth=(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
    )

    if response.status_code == 200:
        with open("images/imagen_recibida.jpg", "wb") as f:
            f.write(response.content)