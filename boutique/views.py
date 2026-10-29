from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Product, Craft, Silhouette
from .serializers import ProductSerializer, CraftSerializer, SilhouetteSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True).order_by('-created_at')
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer

class CraftListAPIView(generics.ListAPIView):
    queryset = Craft.objects.all()
    serializer_class = CraftSerializer

class SilhouetteListAPIView(generics.ListAPIView):
    queryset = Silhouette.objects.all()
    serializer_class = SilhouetteSerializer