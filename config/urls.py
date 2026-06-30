from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🛍️ Product app (home is inside products)
    path('', include('products.urls')),

    # 🛒 Cart
    path('cart/', include('cart.urls')),
]

# 👇 MEDIA FILES (images fix)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)