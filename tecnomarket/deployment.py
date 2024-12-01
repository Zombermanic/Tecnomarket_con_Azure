import os
from .settings import BASE_DIR

# Clave secreta obtenida desde una variable de entorno
SECRET_KEY = os.environ['SECRET']

# Permitir el dominio configurado en Azure
WEBSITE_HOSTNAME = os.environ.get('WEBSITE_HOSTNAME', '')
ALLOWED_HOSTS = [WEBSITE_HOSTNAME] if WEBSITE_HOSTNAME else []

# Proteger el origen de las solicitudes CSRF
CSRF_TRUSTED_ORIGINS = [
    f"https://{WEBSITE_HOSTNAME}"
] if WEBSITE_HOSTNAME else []

# Modo de depuración desactivado en producción
DEBUG = False

# Middleware configurado correctamente
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

# Configuración de la base de datos desde variables de entorno
connection_string = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING', '')
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')} if connection_string else {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters.get('dbname', ''),
        'HOST': parameters.get('host', ''),
        'USER': parameters.get('user', ''),
        'PASSWORD': parameters.get('password', ''),
    }
}
