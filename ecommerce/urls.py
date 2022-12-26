from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from carts.views import OrdersListView
from carts.views import RefundView
from checkout.views import ShippingAddressUpdateView

urlpatterns = [
    path('cart/', include('carts.urls')),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/orders/', OrdersListView.as_view(), name='show-orders'),
    path('accounts/profile/', ShippingAddressUpdateView.as_view(), name='profile'),
    path('refund/', RefundView.as_view(), name='refund'),
    path('', include('Inventory.urls')),
    path('', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
