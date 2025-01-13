#web: python manage.py collectstatic && gunicorn principal.wsgipi

# Realizar collectstatic antes del despliegue (una vez)
release: python manage.py collectstatic --noinput

# Ejecutar la aplicación con multiprocessing optimizado
web: gunicorn principal.wsgipi --workers=4 --preload --bind 0.0.0.0:8000
