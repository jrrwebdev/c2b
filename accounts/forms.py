from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from core.models import Customer


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'category',
                  'address',
                  'city'
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
            'password1': ('Senha'),
            'password2': ('Confirmacão Senha')
        }
        field_classes = {'username': UsernameField}
