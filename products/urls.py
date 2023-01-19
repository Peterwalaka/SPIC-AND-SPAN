from django.urls import path
from .views import HomePage
from .views import ProductDetailView
from.import views
app_name = "products"

urlpatterns = [
    path('help/', views.help, name="help"),
    path('about-us/', views.about_us, name="about-us"),
    path('contact_us/', views.contact, name="contact"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', views.SearchResultsView.as_view(), name="search"),
    path('', HomePage.as_view(), name='home-page'),
    
]

