"""Users views."""

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Models
from apps.users.models import User

# Serializers
from apps.orders.serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    """User viewset."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
