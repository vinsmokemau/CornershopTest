"""Orders serializers."""

# Utilities
from datetime import timedelta
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import User
from apps.orders.models import Order, Option

# Serializer
from apps.users.serializers import UserSerializer
from apps.orders.serializers import OptionSerializer


class OrderSerializer(serializers.ModelSerializer):
    """Menu model serializer."""

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'option',
            'specifications',
        )


class TodayOrderSerializer(serializers.ModelSerializer):
    """Menu model serializer."""

    user = serializers.CharField(
        source='user.username',
        read_only=True,
    )
    option = serializers.CharField(
        source='option.description',
        read_only=True,
    )

    class Meta:
        model = Order
        fields = (
            'user',
            'option',
            'specifications',
        )
