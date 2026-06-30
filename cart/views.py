from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, Order


# ------------------------
# GET SESSION KEY
# ------------------------
def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


# ------------------------
# ADD TO CART
# ------------------------
def add_to_cart(request, product_id):

    session_key = get_session_key(request)

    product = get_object_or_404(Product, id=product_id)

    item, created = Cart.objects.get_or_create(
        session_key=session_key,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart")


# ------------------------
# CART
# ------------------------
def cart_view(request):

    session_key = get_session_key(request)

    items = Cart.objects.filter(
        session_key=session_key
    )

    total = 0

    for item in items:
        item.subtotal = item.product.price * item.quantity
        total += item.subtotal

    return render(request, "cart/cart.html", {
        "items": items,
        "total": total
    })


# ------------------------
# INCREASE
# ------------------------
def increase_quantity(request, item_id):

    session_key = get_session_key(request)

    item = get_object_or_404(
        Cart,
        id=item_id,
        session_key=session_key
    )

    item.quantity += 1
    item.save()

    return redirect("cart")


# ------------------------
# DECREASE
# ------------------------
def decrease_quantity(request, item_id):

    session_key = get_session_key(request)

    item = get_object_or_404(
        Cart,
        id=item_id,
        session_key=session_key
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


# ------------------------
# CHECKOUT
# ------------------------
def checkout(request):

    session_key = get_session_key(request)

    items = Cart.objects.filter(
        session_key=session_key
    )

    total = sum(
        item.product.price * item.quantity
        for item in items
    )

    if request.method == "POST":

        Order.objects.create(
            full_name=request.POST.get("full_name"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            payment_method=request.POST.get("payment_method", "COD"),
            payment_status="Pending",
            payment_screenshot=request.FILES.get("payment_screenshot"),
            total_price=total
        )

        items.delete()

        return redirect("cart")

    return render(request, "cart/checkout.html", {
        "items": items,
        "total": total
    })


# ------------------------
# ORDERS
# ------------------------
def order_history(request):

    orders = Order.objects.all().order_by("-created_at")

    return render(request, "cart/orders.html", {
        "orders": orders
    })