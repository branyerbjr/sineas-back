from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if not data.get('email') or not data.get('password'):
            raise ValidationError({"detail": "Email and password are required."})
        return super().create(request, *args, **kwargs)


class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.filter(email=serializer.validated_data['email']).first()
        if user and user.check_password(serializer.validated_data['password']):
            refresh = RefreshToken.for_user(user)
            user_data = CustomUserSerializer(user).data  # Serialize user data
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'perfil': user_data  # Include user data in the response
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# Ver detalles del usuario autenticado
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'email'
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# Actualizar el usuario autenticado
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
