from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2',

                  )
        labels = {

            'username': ('Nome do usuario (login)'),
            'first_name': ('Primeiro Nome:'),
            'last_name': ('Sobrenome'),
            'email': ('Email'),
            'password1': ('Senha'),
            'password2': ('Confirmacão Senha')
        }

        field_classes = {'username': UsernameField}
