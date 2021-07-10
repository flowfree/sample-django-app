import os 
from .base import *


SECRET_KEY = 'django-insecure-bol)kvaxua908$f-355b%c31w$-to4t&g-2h8x9@e4i(xrn#ee'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
