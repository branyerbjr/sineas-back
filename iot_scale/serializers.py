from rest_framework import serializers


class ControlReleSerializer(serializers.Serializer):
    hora = serializers.CharField(max_length=5)
    estado = serializers.ChoiceField(choices=['on', 'off'])
