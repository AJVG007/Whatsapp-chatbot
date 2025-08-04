from Backend.db_config import SessionLocal
from Backend.models import Contact, Group
from sqlalchemy.exc import IntegrityError

db = SessionLocal()

# Crear grupo primero
group = Group(name="Equipo de Ventas")
db.add(group)
db.commit()
db.refresh(group)  # Necesario para obtener el ID

# Crear contactos con el group_id
contacts_data = [
    {"name": "Alan Baltra", "phone_number": "5215556128917", "group_id": group.id},
    {"name": "Jair Velasco", "phone_number": "5212721310919", "group_id": group.id},
]

for data in contacts_data:
    contact = Contact(**data)
    db.add(contact)

try:
    db.commit()
    print("Grupo y contactos insertados correctamente.")
except IntegrityError as e:
    db.rollback()
    print(f"Error de integridad: {e}")

db.close()