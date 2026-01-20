from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from utils.agent import ask_llama
import requests
import os

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")
    num_media = int(form.get("NumMedia", 0))

    # Pasar mensaje al LLM
    ai_reply = ask_llama(incoming_msg)

    twilio_response = MessagingResponse()
    msg = twilio_response.message()
    msg.body(ai_reply)

    return Response(
        content=str(twilio_response),
        media_type="text/xml"
    )


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