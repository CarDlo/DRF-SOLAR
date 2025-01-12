import os

# Definir todas las variables en un solo lugar
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
