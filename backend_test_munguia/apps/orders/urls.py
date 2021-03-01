"""Orders urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Views
from .views import menus as menu_views
from .views import orders as order_views

app_name = 'orders'

router = routers.DefaultRouter()
router.register(r'menus', menu_views.MenuViewset, basename='menus')
router.register(r'orders', order_views.OrderViewset, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('menu/', menu_views.MenuViewset.as_view({"get": "get_today_menu"})),
    path('editable_menus/', menu_views.MenuViewset.as_view({"get": "get_editable_menus"})),
    path('today_orders/', order_views.OrderViewset.as_view({"get": "get_today_orders"})),
]
