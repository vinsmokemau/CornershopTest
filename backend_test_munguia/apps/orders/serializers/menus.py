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
                menu=menu,
                description=option['description'],
            )
        return menu

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options')
        instance.day = validated_data['day']
        instance.save()
        options = instance.options.all()
        for option, option_data in zip(options, options_data):
            option.description = option_data['description']
            option.save()
        return instance
