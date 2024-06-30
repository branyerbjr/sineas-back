from rest_framework import viewsets
from .models import InitialConfig, UsabilityTutorials, UsageTips, Maintenance, Support
from .serializers import (
    InitialConfigSerializer,
    UsabilityTutorialsSerializer,
    UsageTipsSerializer,
    MaintenanceSerializer,
    SupportSerializer,
)


class InitialConfigViewSet(viewsets.ModelViewSet):
    queryset = InitialConfig.objects.all()
    serializer_class = InitialConfigSerializer


class UsabilityTutorialsViewSet(viewsets.ModelViewSet):
    queryset = UsabilityTutorials.objects.all()
    serializer_class = UsabilityTutorialsSerializer


class UsageTipsViewSet(viewsets.ModelViewSet):
    queryset = UsageTips.objects.all()
    serializer_class = UsageTipsSerializer


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class SupportViewSet(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
