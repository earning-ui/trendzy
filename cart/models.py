from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    payment_method = models.CharField(
        max_length=50,
        default='COD'
    )

    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    payment_screenshot = models.ImageField(
        upload_to='payments/',
        blank=True,
        null=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"