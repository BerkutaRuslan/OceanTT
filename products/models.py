from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Product(models.Model):
    name = models.CharField(max_length=125)
    is_deleted = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product'
