from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HogarViewSet, DispositivoViewSet

router = DefaultRouter()
router.register(r'hogares', HogarViewSet)
router.register(r'dispositivos', DispositivoViewSet)

urlpatterns = [
    path('iot/', include(router.urls)),
]
