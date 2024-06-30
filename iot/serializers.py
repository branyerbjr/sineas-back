from rest_framework import serializers
from .models import Hogar, Dispositivo
from customers.serializers import CustomUserSerializer
from products.serializers import ProductSerializer


class HogarSerializer(serializers.ModelSerializer):
    propietario = CustomUserSerializer(read_only=True)

    class Meta:
        model = Hogar
        fields = '__all__'


class DispositivoSerializer(serializers.ModelSerializer):
    hogar = HogarSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Dispositivo
        fields = '__all__'
