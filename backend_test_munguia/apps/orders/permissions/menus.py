"""Menus permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from apps.orders.models import Menu


class IsNora(BasePermission):
    """Allow access only to Nora's user."""

    def has_permission(self, request, view):
        return (1 == request.user.id) or request.user.is_staff
