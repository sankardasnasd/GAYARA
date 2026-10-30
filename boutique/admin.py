from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Craft, Silhouette, Product

@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Silhouette)
class SilhouetteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'fabric', 'silhouette', 'craft', 'is_available')
    list_filter = ('silhouette', 'craft', 'is_available')
    search_fields = ('name', 'fabric', 'color')




from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'order_number', 'created_at')
    search_fields = ('full_name', 'email', 'order_number', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)