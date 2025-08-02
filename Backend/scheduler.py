from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from sqlalchemy.orm import Session
from Backend.db_config import SessionLocal
from Backend.models import ScheduledMessage, Contact
import httpx
import os

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

scheduler = BackgroundScheduler()

def send_whatsapp_message(phone: str, message: str):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": phone,
        "text": {"body": message}
    }

    # Enviar mensaje (sincrónico por simplicidad)
    response = httpx.post(url, json=payload, headers=headers)
    print(f"Mensaje enviado a {phone} | Estado: {response.status_code}")

def process_scheduled_message(message_id: int):
    db: Session = SessionLocal()
    msg = db.query(ScheduledMessage).filter(ScheduledMessage.id == message_id).first()
    if msg and not msg.sent:
        group = msg.group
        for contact in group.contacts:
            send_whatsapp_message(contact.phone_number, msg.content)

        msg.sent = True
        db.commit()
        print(f"Mensaje {msg.id} marcado como enviado")
    db.close()

def schedule_pending_messages():
    db: Session = SessionLocal()
    messages = db.query(ScheduledMessage).filter(ScheduledMessage.sent == False).all()
    for msg in messages:
        scheduler.add_job(
            func=process_scheduled_message,
            trigger=DateTrigger(run_date=msg.scheduled_time),
            args=[msg.id],
            id=f"msg_{msg.id}",
            replace_existing=True
        )
    db.close()
