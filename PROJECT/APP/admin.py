from django.contrib import admin
from .models import Product,Payment
# Register your models here.
#admin.site.site_header = "Web Tech Store Admin"
admin.site.register(Product)
admin.site.register(Payment)