from fastapi import FastAPI
from Backend.routes import contacts, groups, messages

app = FastAPI()

# Incluir routers
app.include_router(contacts.router)
app.include_router(groups.router)
app.include_router(messages.router)

from Backend.scheduler import scheduler, schedule_pending_messages

@app.on_event("startup")
def startup_event():
    schedule_pending_messages()
    scheduler.start()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o usa solo tu dominio frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)