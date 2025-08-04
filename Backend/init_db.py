from Backend.db_config import SessionLocal
from Backend.models import Contact, Group
from sqlalchemy.exc import IntegrityError

db = SessionLocal()

# Crear grupo primero
group = Group(name="Equipo de Ventas")
db.add(group)
db.commit()
db.refresh(group)  # Obtener ID y sincronizar

# Crear contactos asociándolos por relación, no por group_id directamente
contacts_data = [
    {"name": "Alan Baltra", "phone_number": "5215556128917"},
    {"name": "Tomas Baltra", "phone_number": "5216505165164"},
    {"name": "Jair Velasco", "phone_number": "5212721310919"},
    {"name": "Angel Gallardo", "phone_number": "522721310919"},
]

for data in contacts_data:
    contact = Contact(**data)
    contact.group = group  # ← Asociación correcta usando relación ORM
    db.add(contact)

try:
    db.commit()
    print("Grupo y contactos insertados correctamente.")
except IntegrityError as e:
    db.rollback()
    print(f"Error de integridad: {e}")

db.close()
