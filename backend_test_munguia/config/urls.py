"""Main URLs module."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from apps.utils.healthz import healthz
from django.conf.urls.static import static

urlpatterns = [
    path('', include(('apps.orders.urls', 'orders'), namespace='orders')),
    path('', include(('apps.users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
