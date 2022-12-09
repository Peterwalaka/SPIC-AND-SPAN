# import self as self
from django import forms
from django.forms.fields import CharField
from requests import request




class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First name')
    last_name = forms.CharField(max_length=50, label='Last name')


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = False
        user.save()
        return