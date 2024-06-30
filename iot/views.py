from rest_framework import viewsets
from .models import Hogar, Dispositivo
from .serializers import HogarSerializer, DispositivoSerializer


class HogarViewSet(viewsets.ModelViewSet):
    queryset = Hogar.objects.all()
    serializer_class = HogarSerializer


class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

