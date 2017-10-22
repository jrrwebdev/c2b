from django import forms
from .models import Customer, BuyEvent


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('category',
                  'is_customer',
                  'first_name',
                  'last_name',
                  'email',
                  'address',
                  'city',
                  'state_province',
                  'country',
                  'cnpj_cpf', )

        labels = {
            'category': ('Categoria do produto'),
            'is_customer': ('Tipe de Pessoa'),
            'username': ('Nome do usuario (login)'),
            'first_name': ('Primeiro Nome:'),
            'last_name': ('Sobrenome'),
            'email': ('Email'),
            'address': ('Endereço'),
            'city': ('Cidade '),
            'state_province': ('Estado'),
            'country': ('Pais'),
            'cnpj_cpf': ('CPF/CNPJ'),

        }


class AnunciarForm(forms.ModelForm):
    class Meta:
        model = BuyEvent
        fields = ('name', 'description', 'category', 'price', 'like', 'photo')
