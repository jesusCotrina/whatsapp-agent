# main.py
from fastapi import FastAPI, Request
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")

    response = MessagingResponse()
    reply = response.message()

    # Respuesta simple (luego IA)
    reply.body(f"Recibí tu mensaje: {incoming_msg}")

    return str(response)
