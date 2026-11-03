
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction
from django.core.validators import RegexValidator

from .models import Products, Payments
from . import services


def home_view(request):

    products = Products.objects.all()

    if request.method == "POST":

        phone = request.POST.get("phone", "").strip()
        product_id = request.POST.get("product_id", "").strip()

        # Validate phone number
        if not phone.startswith("254") or len(phone) != 12:
            messages.error(request, "Invalid M-Pesa phone number.")
            return render(
                request,
                "payments/mpesa.html",
                {"products": products}
            )

        try:
            int(phone)
        except ValueError:
            messages.error(request, "Invalid phone number.")
            return render(
                request,
                "payments/mpesa.html",
                {"products": products}
            )

        # Retrieve actual product from database
        product = get_object_or_404(
            Products,
            id=product_id
        )

        amount = product.price

        # Create pending payment record
        payment = Payments.objects.create(
            product=product,
            phone=phone,
            amount=amount,
            status="PENDING"
        )

        try:

            stk = services.STKPUSH(
                phone,
                amount,
                product.product_name
            )

            response = stk.stkpush()

            # Update these fields using the actual
            # response structure returned by your service.

            payment.checkout_request_id = response.get(
                "CheckoutRequestID"
            )

            payment.merchant_request_id = response.get(
                "MerchantRequestID"
            )

            payment.save()

            messages.success(
                request,
                "Payment request sent. Check your phone."
            )

        except Exception:
            payment.status = "FAILED"
            payment.save()

            messages.error(
                request,
                "Unable to initiate payment. Try again."
            )

        return redirect("home")

    return render(
        request,
        "payments/mpesa.html",
        {"products": products}
    )
