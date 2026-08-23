from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Description: {self.description}, Image: {self.image}, Created At: {self.created_at}, Updated At: {self.updated_at}"