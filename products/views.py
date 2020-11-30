from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer, СategorySerializer


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryCreate(generics.CreateAPIView):
    serializer_class = СategorySerializer
    queryset = Product.objects.all()
