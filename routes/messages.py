from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import SessionLocal
from models import ScheduledMessage, Group
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/messages/")
def schedule_message(content: str, scheduled_time: datetime, group_id: int, db: Session = Depends(get_db)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    msg = ScheduledMessage(
        content=content,
        scheduled_time=scheduled_time,
        group_id=group_id,
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return {
        "id": msg.id,
        "content": msg.content,
        "scheduled_time": msg.scheduled_time.isoformat(),
        "group": group.name
    }

@router.get("/messages/")
def list_scheduled_messages(db: Session = Depends(get_db)):
    messages = db.query(ScheduledMessage).all()
    return [
        {
            "id": m.id,
            "content": m.content,
            "scheduled_time": m.scheduled_time.isoformat(),
            "sent": m.sent,
            "group": m.group.name if m.group else None
        }
        for m in messages
    ]
