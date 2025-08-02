from fastapi import FastAPI
from routes import contacts, groups, messages

app = FastAPI()

# Incluir routers
app.include_router(contacts.router)
app.include_router(groups.router)
app.include_router(messages.router)