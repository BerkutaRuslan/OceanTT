from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

    def validate(self, attrs):
        category = attrs.get('category')
        if len(category) < 2:
            msg = 'Product must have atleast two categories'
            raise ValidationError(msg)
        elif len(category) > 10:
            msg = 'Product cannot have more than 10 categories'
            raise ValidationError(msg)
        else:
            return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
