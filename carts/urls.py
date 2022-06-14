from django.urls import path
from .views import increase_product_in_cart, remove_from_cart, decrease_product_in_cart, CartDetailView, AddToCartAjax, GeneratePDF
from .import views

app_name = "carts"

urlpatterns = [
    path('', CartDetailView.as_view(), name='show-cart'),
    path('add/<int:product_id>/', AddToCartAjax.as_view(), name='add-to-cart'),
    path('increase/<int:product_id>/', increase_product_in_cart, name='increase-product-in-cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('decrease/<int:product_id>/', decrease_product_in_cart, name='decrease-product-in-cart'),
    #path('export_csv', views.export_csv, name="export-csv"),
    #path('export_excel', views.export_excel, name="export-excel"),
    #path('order-pdf/', views.order_pdf, name='order-pdf'),
    path('generate-pdf/', GeneratePDF.as_view(), name="generate-pdf"),
]
