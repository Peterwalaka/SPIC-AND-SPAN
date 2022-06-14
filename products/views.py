from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Sell
from django.contrib import messages
#from django.http import HttResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .forms import SellForm




class HomePage(ListView):
    model = Product
    template_name = 'products/nav.html'
    context_object_name = 'products'
    paginate_by = 4

class SellPage(ListView):
      
      model = Sell
      template_name = 'products/sell_list.html'
      context_object_name = 'sells'
      paginate_by = 4
      
      def get(self, request):
          sells = {}
          if request.user.is_superuser:
                sells = Sell.objects.all()
          else:
            sells = Sell.objects.filter(user=request.user)   
          return render(request, self.template_name,{'sells': sells})
      
class SellDetailView(DetailView):
  model = Sell
  template_name = 'products/sell_details.html'      
      
      
      
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
""" 
class SellDetailView(DetailView):
    model = Sell
    template_name = 'products/sell_details.html'    
    
    
def sell_detail(request, pk):
      return render(request, 'sell_details.html', {
    'sell': get_object_or_404(Sell, pk=id)
  })    
"""

 
class SellItem(CreateView):
  model = Sell
  #fields = "__all__"
  form_class = SellForm
  template_name = "products/sell.html"
  success_url = reverse_lazy("products:sell-page")
"""    
  
  def get_sucess_url():
    messages.success('Request Submitted Successfully')
    return redirect('products: sell-page')

class SellItem(CreateView):
  def get(self, request):
    form = SellForm()
    return render(request, 'products/sell.html', {'form': form})
  
  def post(self, request):
    form= SellForm(request.POST)
    if form.is_valid():
          category = form.cleaned_data['category']
          title = form.cleaned_data['title']
          description = form.cleaned_data['description']
          thumbnail = form.cleaned_data['thumbnail ']
          location = form.cleaned_data['location']
          address = form.cleaned_data['address']
          price = form.cleaned_data['price']
          phone_number = form.cleaned_data['phone_number']
          name = form.cleaned_data['name']
          form = Sell(category=category, title=title, description=description, thumbnail=thumbnail, location=location, address=address, price=price, phone_number=phone_number, name=name)
          form.save()
          
          messages.success(request, "Product posted Successfully.")
    return redirect('products:sell-page')
"""    
      