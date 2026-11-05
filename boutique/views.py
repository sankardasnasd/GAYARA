from django.shortcuts import render

# Create your views here.

from rest_framework import generics, settings
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


from django.core.mail import send_mail

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        
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
                fail_silently=False,  
            )
            print(">>> EMAIL SENT SUCCESSFULLY! <<<")
        except Exception as e:
            print(">>> CRITICAL EMAIL ERROR:", repr(e))