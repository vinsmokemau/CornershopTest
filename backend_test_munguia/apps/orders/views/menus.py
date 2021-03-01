"""Menus views."""

# Utilities
import pytz
from datetime import datetime

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from apps.orders.permissions.menus import IsNora

# Models
from apps.orders.models import Menu

# Serializers
from apps.orders.serializers import MenuSerializer


class MenuViewset(viewsets.ModelViewSet):
    """Menu viewset."""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = []
        if self.action in ['create', 'update', 'partial_update', 'get_editable_menus']:
            permissions.append(IsNora)
        return [permission() for permission in permissions]

    @action(detail=True, methods=['get'])
    def get_today_menu(self, request, *args, **kwargs):
        """Retrieve the menu of the current day.

        If the hour is before 11:00a.m. will return 
        a json with the data of the current day's menu.
        """
        utc_now = pytz.utc.localize(datetime.utcnow())
        mex_now = utc_now.astimezone(pytz.timezone("America/Mexico_City"))
        today, time = mex_now.date(), mex_now.time()
        if 11 > time.hour:
            today_menu = Menu.objects.get(day=today)
            data = MenuSerializer(today_menu).data
            return Response(data)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['get'])
    def get_editable_menus(self, request, *args, **kwargs):
        """Retrieve the future menus available to edit.

        If the hour is before 11:00a.m. will return 
        a json with the data of the current day's menu
        and the future ones. If is after 11:00a.m.
        only return the future menus.
        """
        utc_now = pytz.utc.localize(datetime.utcnow())
        mex_now = utc_now.astimezone(pytz.timezone("America/Mexico_City"))
        today, time = mex_now.date(), mex_now.time()
        if 11 > time.hour:
            menus = Menu.objects.filter(day__gte=today)
        else:
            menus = Menu.objects.filter(day__gt=today)
        data = MenuSerializer(menus, many=True).data
        return Response(data)
