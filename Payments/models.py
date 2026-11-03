from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.product_name


class Payments(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("FAILED", "Failed"),
    ]

    product = models.ForeignKey(
        Products,
        on_delete=models.PROTECT
    )

    phone = models.CharField(max_length=12)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    checkout_request_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True
    )

    merchant_request_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.phone}"
