from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
#from django.urls import reverse_lazy
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, View, CreateView
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponse
from carts.utils import render_to_pdf

from products.models import Product
from .models import Order, OrderItem
from .models import RefundForm

import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import *
from django.http import HttpResponse
import csv

from . utils import render_to_pdf
from django.template.loader import get_template
#from xhtml2pdf import pisa
from xhtml2pdf import pisa

from multiprocessing import context

from django.http import FileResponse
import  io
#from reportlab.pdfgen import canvas
#from reportlab.lib.units import inch
#from reportlab.lib.pagesizes import letter
#import xlwt

def order_pdf(request):
    orders = Order.objects.all.filert(user=request.user)
    template_path = 'carts/order_list.html'
    
    context = {'orders':orders}
    
    response = HttpResponse(content_type='application/pdf')
    
    response['content-Disposition'] = 'filename="orders_report.pdf"'
    
    template = get_template(template_path)
    
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        template = get_template('carts/order_list.html')
        context = {
            "orders":orders
        }
        html = template.render(context)
        pdf = render_to_pdf('carts/order_list.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "order_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")






class RefundView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'carts/refund.html'
    form_class = RefundForm
    success_url = reverse_lazy('refund')
    success_message = "The request for a refund has been successfully sent"

    def form_valid(self, form):
        try:
            order = Order.objects.get(order_id=form.cleaned_data['order_id'])
        except Order.DoesNotExist:
            messages.warning(self.request, "Provided order id does not exists")
            return redirect('refund')
        order.refund_requested = True
        order.save()
        form.instance.user = self.request.user
        form.instance.order = order
        return super().form_valid(form)


class OrdersListView(LoginRequiredMixin, ListView):
    context_object_name = 'orders'

    def get_queryset(self):
        return self.request.user.order_set.filter(ordered=True)


class CartDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'order'
    template_name = 'carts/cart.html'

    def get_object(self, queryset=None):
        return self.request.user.order_set.filter(ordered=False).first()


class AddToCartAjax(View):
    def post(self, request, product_id, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return JsonResponse({
                'error': 'In order to make service selections, please create an account'
            }, status=401)
        if self.request.is_ajax:
            product = get_object_or_404(Product, pk=product_id)
            order, _ = Order.objects.get_or_create(user=self.request.user, ordered=False)
            if order.items.filter(item__pk=product_id).exists():
                order_item = order.items.get(item__pk=product_id)
                order_item.quantity += 1
                order_item.save()
            else:
                order_item = OrderItem.objects.create(user=self.request.user, item=product)
                order.items.add(order_item)
            return JsonResponse({
                'msg': "The Service has been successfully selected",
                'quantity': order_item.quantity,
                'total_items': order.get_total_quantity()
            })
        return redirect('carts:show-cart')
     
        


@login_required
def increase_product_in_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
    if order.items.filter(item__pk=product_id).exists():
        order_item = order.items.get(item__pk=product_id)
        order_item.quantity += 1
        order_item.save()
    else:
        order.items.create(user=request.user, item=product)
    messages.success(request, 'Square foot has been added successfully.')
    return redirect('carts:show-cart')
    


@login_required
def decrease_product_in_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order_item.quantity -= 1
            order_item.save()
            if order_item.quantity <= 0:
                order.items.remove(order_item)
            messages.success(request, 'Square foot has been deducted.')
        else:
            messages.warning(request, 'This service is not in your selections.')
    else:
        messages.warning(request, 'Selections do not exist. Add some services to your selections.')
        return redirect('products:home-page')
    return redirect('carts:show-cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order.items.remove(order_item)
            messages.success(request, 'Service has been removed from your selections.')
        else:
            messages.warning(request, 'This Service is not in your selections.')
    else:
        messages.warning(request, 'Selection does not exist. Please select services')
        return redirect('products:home-page')
    return redirect('carts:show-cart')

"""
def export_pdf(request):
    response = HttpResponse(context_type='application/pdf')
    response['Content-Disposition'] = 'attachment: filename=SoldProducts' + \
        str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    
    html_string = render_to_string(
        'carts/pdf-output.html', {'carts': [], 'total':0}
    )  
    html = HTML(string=html_string)
    
    result = html.write_pdf() 
    
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        
        output=open(output.name, 'rb')
        response.write(output.read())
        
    return response    
    
"""    