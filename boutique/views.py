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



from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ContactMessageSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def submit_contact_form(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Message received successfully!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)