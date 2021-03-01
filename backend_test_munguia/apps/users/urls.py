"""Users urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Views
from .views import users as user_views

app_name = 'orders'

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewset, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
