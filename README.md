# WhatsApp Chatbot - Programación de Mensajes

Aplicación web para programar y enviar mensajes automáticos vía WhatsApp Cloud API.

## Tecnologías

- FastAPI (Backend)
- React + Vite (Frontend)
- PostgreSQL (Base de datos)
- WhatsApp Cloud API (Meta)
- Docker & Docker Compose

## Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/tu-usuario/whatsapp-chatbot.git
cd whatsapp-chatbot
```

### 2. Configura el archivo .env en /backend
DATABASE_URL=postgresql://baltra:baltra123@db:5432/baltra
WHATSAPP_TOKEN="tu_token_de_acceso"
WHATSAPP_PHONE_NUMBER_ID="tu_phone_number_id"
APP_ENV=development
PYTHONPATH=/app
SECRET_KEY="your_secret_key_here"
ACCESS_TOKEN_EXPIRE_MINUTES=1440

### 3. Levanta los servicios
```bash
docker-compose up --build
```

### 4. Inserta datos iniciales
```bash
docker-compose exec backend python Backend/init_db.py
```

Autor: Angel Jair Velasco