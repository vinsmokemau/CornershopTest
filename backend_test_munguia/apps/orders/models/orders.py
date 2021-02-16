"""Order model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from apps.utils.models import BaseModel


class Order(BaseModel):
    """
    Order model.
    
    A Order is a | of the current day.
    """

    user = models.ForeignKey(
        'users.User',
        related_name='orders',
        on_delete=models.CASCADE,
    )
    option = models.ForeignKey(
        'orders.Option',
        related_name='orders',
        on_delete=models.CASCADE,
    )
    specifications = models.CharField(
        max_length=150,
        blank=True,
    )
