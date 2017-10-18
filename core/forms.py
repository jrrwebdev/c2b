from django import forms
from .models import Customer, BuyEvent


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('category', 'is_customer')

class AnunciarForm(forms.ModelForm):
    class Meta:
        model = BuyEvent
        fields = ('description', 'price', 'category', 'like', 'photo')
