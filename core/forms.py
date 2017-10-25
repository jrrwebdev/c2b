from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import Saler, Buyer, BuyEvent


class SalerForm(UserCreationForm):
    class Meta:
        model = Saler
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'razaosocial',
                  'address',
                  'city',
                  'state_province',
                  'country',
                  'cnpj',
                  'ie'
                  )

        labels = {
            'username': ('Nome do usuario (login)'),
            'razaosocial': ('Razao Social'),
            'email': ('Email'),
            'address': ('Endereço'),
            'city': ('Cidade '),
            'state_province': ('Estado'),
            'country': ('Pais'),
            'cnpj': ('CNPJ:'),
            'ie': ('IE'),
        }
        # field_classes = {'username': UsernameField}


class BuyerForm(UserCreationForm):
    class Meta:
        model = Buyer
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'name',
                  'address',
                  'city',
                  'state_province',
                  'country',
                  'rg',
                  'cpf',
                  )

        labels = {
            'username': ('Nome do usuario (login)'),
            'first_name': ('Primeiro Nome:'),
            'last_name': ('Sobrenome'),
            'email': ('Email'),
            'address': ('Endereço'),
            'city': ('Cidade '),
            'state_province': ('Estado'),
            'country': ('Pais'),
            'rg': ('RG'),
            'cpf': ('CPF'),
        }
        # field_classes = {'username': UsernameField}


class AnunciarForm(forms.ModelForm):
    class Meta:
        model = BuyEvent
        fields = ('name', 'price', 'photo')
        labels = {
            'name': ('Produto Desejado'),
            'description': ('Descricao'),
            'price': ('Preco Desejado'),
            'photo': ('Fotografia')
        }
