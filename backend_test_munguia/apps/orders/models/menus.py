"""Menu models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from apps.utils.models import BaseModel


class Menu(BaseModel):
    """
    Menu model.
    
    A Menu is a collection of meal options for one day.
    """

    day = models.DateField()


class Option(BaseModel):
    """
    Option model.
    
    An Option is a specific meal of a menu.
    """

    menu = models.ForeignKey(
        'Menu',
        related_name='options',
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.description
