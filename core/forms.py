from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import Vendedor, Comprador, EventoCompra


class VendedorForm(UserCreationForm):
    class Meta:
        model = Vendedor
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'razaosocial',
                  'endereco',
                  'cidade',
                  'estado',
                  'pais',
                  'cnpj',
                  'ie'
                  )

        labels = {
            'username': ('Nome do usuario (login)'),
            'razaosocial': ('Razao Social'),
            'email': ('Email'),
            'endereco': ('Endereço'),
            'cidade': ('Cidade '),
            'estado': ('Estado'),
            'pais': ('Pais'),
            'cnpj': ('CNPJ:'),
            'ie': ('IE'),
        }
        # field_classes = {'username': UsernameField}


class CompradorForm(UserCreationForm):
    class Meta:
        model = Comprador
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'nome',
                  'endereco',
                  'cidade',
                  'estado',
                  'pais',
                  'rg',
                  'cpf',
                  )

        labels = {
            'username': ('Nome do usuario (login)'),
            'nome': ('Nome'),
            'email': ('Email'),
            'endereco': ('Endereço'),
            'cidade': ('Cidade '),
            'estado': ('Estado'),
            'pais': ('Pais'),
            'rg': ('RG'),
            'cpf': ('CPF'),
        }
        # field_classes = {'username': UsernameField}


class AnunciarForm(forms.ModelForm):
    class Meta:
        model = EventoCompra
        fields = ('nomeproduto', 'categoriaproduto', 'preco', 'imagemproduto')
        labels = {
            'nomeproduto': ('Produto Desejado'),
            'descricao': ('Descricao'),
            'preco': ('Preco Desejado'),
            'imagemproduto': ('Fotografia')
        }
