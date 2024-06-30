from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy, PurchaseCreate, ProductListByCustomer

urlpatterns = [
    # URLs para productos
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),

    # URL para crear una compra
    path('purchase/', PurchaseCreate.as_view(), name='purchase-create'),

    # URL para ver los productos de un cliente específico
    path('products/customer/', ProductListByCustomer.as_view(), name='product-list-by-customer'),
]

