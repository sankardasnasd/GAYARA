from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import ContactMessage, Product, Craft, Silhouette
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




from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {"message": "Thank you! Your message has been received."},
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        instance = serializer.save()
        
        # Email Notification Sending
        try:
            subject = f"🌸 New GAYARA Message: {instance.subject}"
            body = (
                f"You have received a new contact message:\n\n"
                f"Name: {instance.full_name}\n"
                f"Email: {instance.email}\n"
                f"Order Number: {instance.order_number or 'Not provided'}\n\n"
                f"Message:\n{instance.message}\n"
            )
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['contactgayara@gmail.com'],
                fail_silently=True,
            )
        except Exception as e:
            print("Email sending error:", e)