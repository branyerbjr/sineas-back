from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Purchase
from .serializers import ProductSerializer, PurchaseSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchaseCreate(generics.CreateAPIView):
    serializer_class = PurchaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = request.user  # Assuming you are using authentication
        product_id = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        if product.estoque < quantity:
            return Response({"error": "No hay suficiente stock disponible."}, status=status.HTTP_400_BAD_REQUEST)

        # Create purchase record
        Purchase.objects.create(customer=customer, product=product, quantity=quantity)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductListByCustomer(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(purchase__customer=user)
