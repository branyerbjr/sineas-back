from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, UserDetailAPIView, UserUpdateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
]