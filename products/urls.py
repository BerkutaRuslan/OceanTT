from django.urls import path

from products.views import ProductCreateView, CategoryCreateView, ProductUpdateView, ProductDeleteView, \
    DeleteCategoryView

urlpatterns = [
    path('create', ProductCreateView.as_view()),
    path('create/category', CategoryCreateView.as_view()),
    path('update/<int:pk>', ProductUpdateView.as_view()),
    path('delete/<int:pk>', ProductDeleteView.as_view()),
    path('delete/category/<int:pk>', DeleteCategoryView.as_view())
]