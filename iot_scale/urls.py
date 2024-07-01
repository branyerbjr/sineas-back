from django.urls import path
from .views import control_relay

urlpatterns = [
    path('control/', control_relay, name='control_relay'),
]