from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from agent import ask_llama

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")

    # 👉 Pasar mensaje al LLM
    ai_reply = ask_llama(incoming_msg)

    twilio_response = MessagingResponse()
    msg = twilio_response.message()
    msg.body(ai_reply)

    return Response(
        content=str(twilio_response),
        media_type="text/xml"
    )
