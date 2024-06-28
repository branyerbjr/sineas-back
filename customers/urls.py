# customers/urls.py
from django.urls import path
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy

urlpatterns = [
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
]
