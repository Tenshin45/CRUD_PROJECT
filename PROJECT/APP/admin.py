from django.contrib import admin
from .models import Product, Payment, ContactMessage


admin.site.register(Product)
admin.site.register(Payment)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'subject',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'subject',
    )

    ordering = ('-created_at',)