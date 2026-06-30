from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🏠 Home page (ONLY HERE)
    path('', views.home, name='home'),

    # 🛍️ Product app
    path('', include('products.urls')),

    # 🛒 Cart
    path('cart/', include('cart.urls')),

    # 👤 Accounts
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )