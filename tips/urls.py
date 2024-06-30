from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InitialConfigViewSet,
    UsabilityTutorialsViewSet,
    UsageTipsViewSet,
    MaintenanceViewSet,
    SupportViewSet,
)

router = DefaultRouter()
router.register(r'initial-configs', InitialConfigViewSet)
router.register(r'usability-tutorials', UsabilityTutorialsViewSet)
router.register(r'usage-tips', UsageTipsViewSet)
router.register(r'maintenance', MaintenanceViewSet)
router.register(r'support', SupportViewSet)

urlpatterns = [
    path('tips/', include(router.urls)),
]
