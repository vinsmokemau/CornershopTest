"""Menus views."""

# Utilities
import pytz
from datetime import datetime

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from apps.orders.models import Menu

# Serializers
from apps.orders.serializers import MenuSerializer


class MenuViewset(viewsets.ModelViewSet):
    """Menu viewset."""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

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
