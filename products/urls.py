from django.urls import path
from .views import HomePage
from .views import ProductDetailView
from.import views
#from carts.views import AddToCartAjax
app_name = "products"

urlpatterns = [
    path('help/', views.help, name="help"),
    path('about-us/', views.about_us, name="about-us"),
    path('contact_us/', views.contact, name="contact"),
    path('', HomePage.as_view(), name='home-page'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', views.SearchResultsView.as_view(), name="search"),

    #path("sell-item/", views.SellItem.as_view(), name="sell-item"),
    #path('sell/<int:pk>/', SellDetailView.as_view(), name='sell-detail')
    #path('sell-detail', views.sell_detail, name='sell-detail'),
    #path('add/<int:product_id>/', AddToCartAjax.as_view(), name='add-to-cart'),
    
]

