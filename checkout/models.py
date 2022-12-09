from django.db import models
from django import forms
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    ward = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    residence_name = models.CharField(max_length=100)
    cleaning_date = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    current_address = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Service address'
        verbose_name_plural = 'Service addresses'

    def __str__(self):
        return f'Cleaning address for {self.user.first_name} {self.user.last_name}: {self.sub_county} {self.ward} {self.residence_name}  {self.cleaning_date} {self.phone},'

    def get_absolute_url(self):
        return reverse('profile')


class ShippingAddressForm(forms.ModelForm):
    save_address = forms.BooleanField(required=False, label='Save the billing address')

    class Meta:

        model = ShippingAddress
        fields = [
            'first_name',
            'last_name',
            'sub_county',
            'ward',
            'residence_name',
            'cleaning_date',
            'phone',
        ]


class Payment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_id = models.CharField(max_length=60)
    amount = models.FloatField()
    issued_data = models.DateTimeField(auto_now_add=True)
    approval = models.BooleanField('approval', default=False)



    class Meta:
        verbose_name = 'Finance'
        verbose_name_plural = 'Finances'


    def __str__(self):
        return f'{self.user} payment: {self.amount}, {self.approval}'






class PromotionCode(models.Model):
    code = models.CharField(max_length=50)
    percentage_discount = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.code


class PromotionCodeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].required = False

    class Meta:
        model = PromotionCode
        fields = ['code']
        labels = {
            'code': 'Promotion Code'
        }
