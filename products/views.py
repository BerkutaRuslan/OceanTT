from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer, CategorySerializer


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Product.objects.all()
