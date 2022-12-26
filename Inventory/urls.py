from django.urls import path

from Inventory.views import OrderPdfView

urlpatterns = [
    path('order-pdf/<int:pk>/', OrderPdfView.as_view(), name="order-pdf")
]