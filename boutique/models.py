from django.db import models

# Create your models here.
from django.db import models

class Craft(models.Model):
    name = models.CharField(max_length=100) # ഉദാ: Chikankari, Kantha, Kashmiri Aari

    def __str__(self):
        return self.name

class Silhouette(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    fabric = models.CharField(max_length=120) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    silhouette = models.ForeignKey(Silhouette, on_delete=models.SET_NULL, null=True, related_name='products')
    craft = models.ForeignKey(Craft, on_delete=models.SET_NULL, null=True, related_name='products')
    color = models.CharField(max_length=50, blank=True) 
    image = models.ImageField(upload_to='dresses/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name