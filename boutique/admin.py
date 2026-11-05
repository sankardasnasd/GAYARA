from django.contrib import admin
from .models import Craft, Silhouette, Product, ContactMessage

@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Silhouette)
class SilhouetteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'craft', 'fabric', 'available_sizes', 'is_available')
    list_filter = ('craft', 'is_available', 'silhouette')
    search_fields = ('name', 'description', 'fabric')
    list_editable = ('price', 'is_available')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'order_number', 'created_at')
    search_fields = ('full_name', 'email', 'order_number', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)