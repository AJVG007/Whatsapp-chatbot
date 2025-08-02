FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Cargar variables de entorno
ENV PYTHONUNBUFFERED=1

# Ejecutar servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
