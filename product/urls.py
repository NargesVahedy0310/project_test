from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryDetailView,
    FileListView,
    FileDetailView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/', CategoryListView.as_view(), name='category-view'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),


    path('products/<int:product_id>/files/', FileListView.as_view(), name='file-view'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),


    path('category/<int:product_id>/files/', FileListView.as_view(), name='file-view'),
    path('category/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
]