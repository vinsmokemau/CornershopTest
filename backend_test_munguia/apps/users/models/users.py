"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from apps.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """
    User model.
    
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username
