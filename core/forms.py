from django import forms
from .models import Customer, BuyEvent
from utils.lists import CUSTOMER_TYPE, IS_CUSTOMER


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('is_customer',
                  'person_type',
                  'category',
                  'first_name',
                  'last_name',
                  'email',
                  'address',
                  'city',
                  'state_province',
                  'country',
           )

        labels = {
            'category': ('Categoria do produto'),
            'is_customer': ('Tipo de Cliente'),
            'person_type': ('Tipo de Pessoa'),
            'username': ('Nome do usuario (login)'),
            'first_name': ('Primeiro Nome:'),
            'last_name': ('Sobrenome'),
            'email': ('Email'),
            'address': ('Endereço'),
            'city': ('Cidade '),
            'state_province': ('Estado'),
            'country': ('Pais'),
        }
        exclude = ['password']


class AnunciarForm(forms.ModelForm):
    class Meta:
        model = BuyEvent
        fields = ('name', 'description', 'category', 'price', 'like', 'photo')
