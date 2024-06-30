from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'username', 'password', 'uuid_google',
            'profile_picture', 'first_name', 'last_name', 'is_active',
            'is_staff', 'is_superuser'
        ]
# read_only_fields = ['id', 'email', 'date_joined', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
