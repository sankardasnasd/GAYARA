from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CraftListAPIView, SilhouetteListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('crafts/', CraftListAPIView.as_view(), name='craft-list'),
    path('silhouettes/', SilhouetteListAPIView.as_view(), name='silhouette-list'),
]