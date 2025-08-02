FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

# Ejecutar uvicorn con PYTHONPATH y ruta correcta al módulo
CMD ["bash", "-c", "PYTHONPATH=/app uvicorn Backend.main:app --host 0.0.0.0 --port 8000 --reload"]

