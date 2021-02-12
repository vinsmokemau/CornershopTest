"""Development settings."""

import os
from .base import *  # NOQA

# Base
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = True

# Security
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405
