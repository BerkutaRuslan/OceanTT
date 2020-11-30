from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Product(models.Model):
    name = models.CharField(max_length=125)
    price = models.FloatField(blank=False, null=False)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product'
