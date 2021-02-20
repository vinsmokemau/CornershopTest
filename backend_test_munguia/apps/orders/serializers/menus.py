"""Menus serializers."""

# Utilities
from datetime import timedelta
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers

# Models
from apps.orders.models import Menu, Option


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = (
            'id',
            'description',
        )


class MenuSerializer(serializers.ModelSerializer):
    """Menu model serializer."""

    options = OptionSerializer(
        many=True,
    )

    class Meta:
        model = Menu
        fields = (
            'id',
            'day',
            'options',
        )

    def create(self, validated_data):
        options = validated_data.pop('options')
        menu = Menu.objects.create(**validated_data)
        for option in options:
            Option.objects.create(
                menu = menu,
                description = option['description'],
            )
        return menu
