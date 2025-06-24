# 1. Usar una imagen base oficial de Python
FROM python:3.11-slim-bullseye

# 2. Variables de entorno para que Python corra mejor en Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar el archivo de dependencias
COPY requirements.txt .

# 5. Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt
