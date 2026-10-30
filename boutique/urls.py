from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CraftListAPIView, SilhouetteListAPIView,submit_contact_form

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('crafts/', CraftListAPIView.as_view(), name='craft-list'),
    path('silhouettes/', SilhouetteListAPIView.as_view(), name='silhouette-list'),

    path('contact/', submit_contact_form, name='contact-submit'),
]