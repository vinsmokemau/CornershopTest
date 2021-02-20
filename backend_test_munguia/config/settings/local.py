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

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://0.0.0.0:8080',
    'http://127.0.0.1:8080',
)

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Fixtures
FIXTURE_DIRS = (
    'apps/users/fixtures/users.json',
)

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405
