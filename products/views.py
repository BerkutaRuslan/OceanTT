from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer, CategorySerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Product.objects.all()


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.filter(is_deleted=False)


class ProductDeleteView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.is_deleted = True
            product.save()
            return Response({'message': 'Product status was updated to deleted.'}, status=status.HTTP_200_OK)
        except product.DoesNotExist:
            msg = 'Product does not exists'
            raise ValidationError(msg)




