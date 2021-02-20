"""Orders views."""

# Utilities
import pytz
from datetime import datetime

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from apps.orders.models import Order

# Serializers
from apps.orders.serializers import (
    OrderSerializer,
    TodayOrderSerializer,
)


class OrderViewset(viewsets.ModelViewSet):
    """Order viewset."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['get'])
    def get_today_orders(self, request, *args, **kwargs):
        """Retrieve a list of orders of the current day."""
        utc_now = pytz.utc.localize(datetime.utcnow())
        mex_now = utc_now.astimezone(pytz.timezone("America/Mexico_City"))
        today, time = mex_now.date(), mex_now.time()
        today_orders = Order.objects.filter(created__date=today)
        data = TodayOrderSerializer(today_orders, many=True).data
        return Response(data)

    def create(self, request, *args, **kwargs):
        utc_now = pytz.utc.localize(datetime.utcnow())
        mex_now = utc_now.astimezone(pytz.timezone("America/Mexico_City"))
        today, time = mex_now.date(), mex_now.time()
        if 11 > time.hour:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
