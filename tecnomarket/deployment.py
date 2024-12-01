import os
from .settings import BASE_DIR

# Clave secreta desde las variables de entorno
SECRET_KEY = os.environ['SECRET']

import os

ALLOWED_HOSTS = [
    os.environ.get('WEBSITE_HOSTNAME', ''),  # Dominio proporcionado automáticamente por Azure
    'localhost',  # Para pruebas locales
]

CSRF_TRUSTED_ORIGINS = [
    'https://' + os.environ.get('WEBSITE_HOSTNAME', ''),  # Dominio proporcionado automáticamente por Azure
]


DEBUG = False

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de base de datos desde una variable de entorno
connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST': parameters['host'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
    }
}
