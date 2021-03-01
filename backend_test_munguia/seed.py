"""Seed data to the db."""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

# Django
import django
django.setup()

# User's Model
from apps.users.models import User

try:
    nora = User.objects.create_user(
        username='bigboss',
        first_name='nora_cornershop',
        last_name='X',
        email='nora@cornershopapp.com',
        is_staff=True,
        is_active=True,
        is_superuser=True,
        password='nora_pass_1234',
    )
    nora.save()
    backend_user = User.objects.create_user(
        username='backendev',
        first_name='Backend',
        last_name='Developer',
        email='backendev@cornershopapp.com',
        password='back_dev_1234',
        is_active=True,
    )
    backend_user.save()
    frontend_user = User.objects.create_user(
        username='frontendev',
        first_name='Frontend',
        last_name='Developer',
        email='frontendev@cornershopapp.com',
        password='front_dev_1234',
        is_active=True,
    )
    frontend_user.save()
except:
    pass
