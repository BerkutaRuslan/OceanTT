from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


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
        except Product.DoesNotExist:
            msg = 'Product does not exists'
            raise ValidationError(msg)


class DeleteCategoryView(APIView):
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            if category.products.all():
                msg = 'You cannot delete this category, because it has relation with a product'
                return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)
            else:
                category.delete()
                msg = 'Category was deleted successfully'
                return Response({'message': msg}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            msg = 'Category does not exists'
            raise ValidationError(msg)
