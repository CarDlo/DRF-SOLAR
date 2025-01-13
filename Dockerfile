# Usar la imagen oficial de Python como base
FROM python:3.11-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Instalar las dependencias del sistema necesarias (como libpq-dev si usas PostgreSQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requisitos de tu aplicación (si tienes uno)
COPY requirements.txt /app/

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al contenedor
COPY . /app/

# Establecer las variables de entorno, si no están configuradas en Railway
ENV SECRET_KEY=${SECRET_KEY}
ENV DATABASE_URL=${DATABASE_URL}
ENV DJANGO_SETTINGS_MODULE=principal.settings

# Realizar collectstatic antes del despliegue (una vez)
RUN python manage.py collectstatic --noinput

# Exponer el puerto 8000 para que el contenedor sea accesible
EXPOSE 8000

# Ejecutar Gunicorn con múltiples trabajadores (multiprocessing)
CMD ["gunicorn", "principal.wsgi:application", "--workers", "4", "--preload", "--bind", "0.0.0.0:8000"]
