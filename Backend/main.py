from fastapi import FastAPI
from Backend.routes import contacts, groups, messages
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# Incluir routers
app.include_router(messages.router, prefix="/api")
app.include_router(groups.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")



from Backend.scheduler import scheduler, schedule_pending_messages

@app.on_event("startup")
def startup_event():
    from Backend.db_config import Base, engine
    from Backend import models
    Base.metadata.create_all(bind=engine)

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