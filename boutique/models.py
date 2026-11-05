from django.db import models

class Craft(models.Model):
    name = models.CharField(max_length=100)

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
    available_sizes = models.CharField(
        max_length=100, 
        default='XS, S, M, L, XL', 
        help_text="Comma-separated sizes (e.g. S, M, L)"
    )
    image = models.ImageField(upload_to='dresses/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    order_number = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']