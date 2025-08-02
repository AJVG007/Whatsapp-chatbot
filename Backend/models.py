from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from Backend.db_config import Base
from datetime import datetime

# Tabla intermedia grupo-contactos
group_contact = Table(
    "group_contact", Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.id")),
    Column("contact_id", Integer, ForeignKey("contacts.id")),
)

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contacts = relationship("Contact", secondary=group_contact, backref="groups")

class ScheduledMessage(Base):
    __tablename__ = "scheduled_messages"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    scheduled_time = Column(DateTime)
    sent = Column(Boolean, default=False)
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group")
