from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product


# ----------------------
# 🏠 HOME PAGE
# ----------------------
def home(request):
    query = request.GET.get('q', '')  # safe default

    # default products (latest 8)
    products = Product.objects.all().order_by('-created_at')[:8]

    # search feature
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).order_by('-created_at')

    return render(request, 'home.html', {
        'products': products,
        'query': query
    })


# ----------------------
# 🛍️ PRODUCT LIST PAGE
# ----------------------
def product_list(request):
    products = Product.objects.all().order_by('-created_at')

    return render(request, 'products/product_list.html', {
        'products': products
    })


# ----------------------
# 📦 PRODUCT DETAIL PAGE
# ----------------------
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'products/product_detail.html', {
        'product': product
    })