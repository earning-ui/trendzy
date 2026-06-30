from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product


# 🏠 HOME PAGE
def home(request):
    query = request.GET.get('q')

    products = Product.objects.all()[:8]

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'home.html', {'products': products})


# 🛍️ PRODUCT LIST PAGE
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


# 📦 PRODUCT DETAIL PAGE
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})