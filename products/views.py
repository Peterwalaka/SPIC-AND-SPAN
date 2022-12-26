from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


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
