from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Contact
from db_config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/contacts/")
def create_contact(name: str, phone_number: str, db: Session = Depends(get_db)):
    contact = Contact(name=name, phone_number=phone_number)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

@router.get("/contacts/")
def list_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()
