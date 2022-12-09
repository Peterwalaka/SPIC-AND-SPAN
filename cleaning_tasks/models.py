from django.db import models
from django.conf import settings
from django import forms

from carts.models import Order
from products.models import Product
from checkout.models import ShippingAddress
from checkout.models import Payment


# Create your models here.


class FieldSupervisionTasks(models.Model):
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    allocated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Field Supervision Task'
        verbose_name_plural = 'Field Supervision Tasks'

    def __str__(self):
        return f'{self.user.username}: {self.description}: {self.order_id}: {self.allocated_on}'


class CleaningTasks(models.Model):
    description = models.TextField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    allocated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cleaning Task'
        verbose_name_plural = 'Cleaning Tasks'

    def __str__(self):
        return f' {self.description} {self.order_id} {self.allocated_on}'

