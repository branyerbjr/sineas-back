# products/admin.py
from django.contrib import admin
from .models import Product, Purchase

# Registrar los modelos aquí
admin.site.register(Product)
admin.site.register(Purchase)
