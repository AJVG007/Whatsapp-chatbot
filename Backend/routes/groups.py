from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from Backend.models import Group, Contact
from Backend.db_config import SessionLocal

router = APIRouter()

# Modelo Pydantic para recibir datos JSON
class GroupCreate(BaseModel):
    name: str
    contact_ids: List[int]

# Dependencia para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear grupo
@router.post("/groups/")
def create_group(data: GroupCreate, db: Session = Depends(get_db)):
    contacts = db.query(Contact).filter(Contact.id.in_(data.contact_ids)).all()
    if not contacts:
        raise HTTPException(status_code=404, detail="No valid contacts found")

    group = Group(name=data.name, contacts=contacts)
    db.add(group)
    db.commit()
    db.refresh(group)
    return {
        "id": group.id,
        "name": group.name,
        "contacts": [{"id": c.id, "name": c.name, "phone": c.phone_number} for c in group.contacts]
    }

# Listar grupos
@router.get("/groups/")
def list_groups(db: Session = Depends(get_db)):
    groups = db.query(Group).all()
    return [
        {
            "id": g.id,
            "name": g.name,
            "contacts": [{"id": c.id, "name": c.name, "phone": c.phone_number} for c in g.contacts]
        }
        for g in groups
    ]
