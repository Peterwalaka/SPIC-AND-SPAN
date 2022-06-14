from django.urls import path
from .views import HomePage
from .views import ProductDetailView,SellDetailView, SellPage
from.import views
#from carts.views import AddToCartAjax
app_name = "products"

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    #path("sell-item/", views.SellItem.as_view(), name="sell-item"),
    path('sell/<int:pk>/',SellDetailView.as_view(), name='sell-detail' ),
    path('sell-page/', views.SellPage.as_view(), name='sell-page'),
    path('sell-item/', views.SellItem.as_view(), name="sell-item"),
    #path('sell/<int:pk>/', SellDetailView.as_view(), name='sell-detail')
    #path('sell-detail', views.sell_detail, name='sell-detail'),
    #path('add/<int:product_id>/', AddToCartAjax.as_view(), name='add-to-cart'),
    
]
