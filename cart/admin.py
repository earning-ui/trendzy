from django.contrib import admin
from .models import Cart, Order


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "session_key",
        "product",
        "quantity",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("session_key",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "phone",
        "payment_method",
        "payment_status",
        "total_price",
        "created_at",
    )
    list_filter = ("payment_status", "payment_method", "created_at")
    search_fields = ("full_name", "phone")