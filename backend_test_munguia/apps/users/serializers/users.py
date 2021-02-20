"""Users serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
