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

class Payment(models.Model):
    Phone_Number=models.CharField(max_length=15)
    Amount=models.DecimalField(max_digits=10,decimal_places=2)
    Status=models.CharField(max_length=20,default="Pending")
    Merchant_id=models.CharField(max_length=100,blank=True,null=True)
    Created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Number is :{self.Phone_Number} Amount :{self.Amount} Created at :{self.Created_at}'    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"