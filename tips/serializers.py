from rest_framework import serializers
from .models import InitialConfig, UsabilityTutorials, UsageTips, Maintenance, Support


class InitialConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialConfig
        fields = '__all__'


class UsabilityTutorialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsabilityTutorials
        fields = '__all__'


class UsageTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageTips
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'
