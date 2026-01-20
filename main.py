from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")

    twilio_response = MessagingResponse()
    msg = twilio_response.message()
    msg.body(f"Recibí tu mensaje: {incoming_msg}")

    return Response(
        content=str(twilio_response),
        media_type="text/xml"
    )
