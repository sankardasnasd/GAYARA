from rest_framework import serializers
from .models import Craft, Silhouette, Product

class CraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craft
        fields = ['id', 'name']

class SilhouetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silhouette
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    craft_name = serializers.ReadOnlyField(source='craft.name')
    silhouette_name = serializers.ReadOnlyField(source='silhouette.name')

    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'description', 
            'fabric', 
            'price', 
            'color', 
            'image', 
            'is_available', 
            'craft', 
            'craft_name', 
            'silhouette', 
            'silhouette_name',
            'created_at'
        ]