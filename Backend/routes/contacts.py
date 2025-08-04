from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Backend.models import Contact
from Backend.db_config import SessionLocal

router = APIRouter()

# Modelo de entrada para crear contacto
class ContactCreate(BaseModel):
    name: str
    phone_number: str

# Conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear contacto
@router.post("/contacts/")
def create_contact(data: ContactCreate, db: Session = Depends(get_db)):
    contact = Contact(name=data.name, phone_number=data.phone_number)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return {
        "id": contact.id,
        "name": contact.name,
        "phone_number": contact.phone_number
    }

# Listar contactos
@router.get("/contacts/")
def list_contacts(db: Session = Depends(get_db)):
    return [
        {
            "id": c.id,
            "name": c.name,
            "phone_number": c.phone_number
        }
        for c in db.query(Contact).all()
    ]
