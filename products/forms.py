from django import forms
from django.forms.fields import CharField
from .models import Sell

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'