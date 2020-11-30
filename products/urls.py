from django.urls import path

from products.views import ProductCreate, CategoryCreate

urlpatterns = [
    path('create', ProductCreate.as_view()),
    path('create/category', CategoryCreate.as_view()),
]