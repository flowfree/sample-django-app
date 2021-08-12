import os 
from .base import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']

if 'WEBSITE_HOSTNAME' in os.environ:
    ALLOWED_HOSTS = [os.getenv('WEBSITE_HOSTNAME')]
if 'APP_HOSTNAME' in os.environ:
    ALLOWED_HOSTS = [os.getenv('APP_HOSTNAME')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', 5432),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

# Disable Browsable API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
