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