from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, Order
from django.contrib.auth.decorators import login_required

def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')


def cart_view(request):

    items = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in items:
        item.subtotal = (
            item.product.price *
            item.quantity
        )

        total += item.subtotal

    return render(
        request,
        'cart/cart.html',
        {
            'items': items,
            'total': total
        }
    )


def increase_quantity(request, item_id):

    item = get_object_or_404(
        Cart,
        id=item_id,
        user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('cart')


def decrease_quantity(request, item_id):

    item = get_object_or_404(
        Cart,
        id=item_id,
        user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'cart/orders.html',
        {
            'orders': orders
        }
    )


def checkout(request):

    items = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in items:
        total += (
            item.product.price *
            item.quantity
        )

    if request.method == "POST":

        full_name = request.POST.get(
            'full_name'
        )

        phone = request.POST.get(
            'phone'
        )

        address = request.POST.get(
            'address'
        )

        payment_method = request.POST.get(
            'payment_method',
            'COD'
        )

        payment_screenshot = request.FILES.get(
            'payment_screenshot'
        )

        Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            address=address,
            payment_method=payment_method,
            payment_status='Pending',
            payment_screenshot=payment_screenshot,
            total_price=total
        )

        items.delete()

        return redirect('orders')

    return render(
        request,
        'cart/checkout.html',
        {
            'items': items,
            'total': total
        }
    )