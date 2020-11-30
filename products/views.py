from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.filter(is_deleted=False)


class ProductDeleteView(APIView):

    @swagger_auto_schema(
        operation_id='Delete Product',
        operation_description="Endpoint for deleting Product by id",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,

        ),
        responses={
            200: 'OK',
        },
        security=[],
        tags=['products'],
    )
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
    @swagger_auto_schema(
        operation_id='Delete Category',
        operation_description="Endpoint for deleting Category by id",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,

        ),
        responses={
            200: 'OK',
        },
        security=[],
        tags=['category'],
    )
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


class ListProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        name = self.request.GET.get("name")
        category_id = self.request.GET.get('category_id')
        is_published = self.request.GET.get('is_published')
        sort_min_max = self.request.GET.get('sort_min_max')
        sort_max_min = self.request.GET.get('sort_max_min')
        if name:
            products = products.filter(name=name)
        if category_id:
            products = products.filter(category=category_id)
        if sort_min_max:
            products = products.order_by('price')
        if sort_max_min:
            products = products.order_by('-price')
        if is_published:
            products = products.filter(is_published=is_published)
        return products.filter(is_deleted=False)

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        """
        Url for listing info about products, accepts query params like:
        name= , category_id= , is_published= , sort_min_max = True/False,  sort_max_min = True/False,
        is_published = True/False.
        Example url: http://127.0.0.1:8000/products/list-products?category_id=3&name=Pizza&is_published=True&sort_min_max=True
        """
        return super().get(request, args, kwargs)
