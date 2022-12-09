from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Product
from django.contrib import messages
#from django.http import HttResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy


class HomePage(ListView):
    model = Product
    template_name = 'products/nav.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 4

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_details.html'

class SearchResultsView(ListView):
    model = Product
    template_name = 'products/nav.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(name__icontains=query)


def contact(request):
    context = {
        "contact": contact,
        }
    return render(request, 'products/contact.html', context)

def about_us(request):
    context = {
        "about_us": about_us,
    }
    return render(request, 'products/about_us.html', context)

def help(request):
    context = {
        "help": help,
    }
    return render(request, 'products/help.html', context)





""" 
class SellDetailView(DetailView):
    model = Sell
    template_name = 'products/sell_details.html'    
    
    
def sell_detail(request, pk):
      return render(request, 'sell_details.html', {
    'sell': get_object_or_404(Sell, pk=id)
  })    
"""

 

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
      