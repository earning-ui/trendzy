from django.contrib import admin
from .models import Cart, Order

admin.site.register(Cart)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'payment_method',
        'payment_status',
        'total_price',
        'created_at'
    )