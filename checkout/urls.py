from django.urls import path
from .views import CheckoutView, checkout_success, PaymentView, PromoCodeView


app_name = "checkout"

urlpatterns = [
    path('payment/', PaymentView.as_view(), name='payment'),
    path('success/', checkout_success, name='checkout-success'),
    path('add-promotion-code/', PromoCodeView.as_view(), name='promotion-code'),
    path('', CheckoutView.as_view(), name='checkout'),
]
