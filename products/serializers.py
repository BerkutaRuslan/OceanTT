from rest_framework import serializers
from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class СategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
