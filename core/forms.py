from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    CLIENTE = 1
    EMPRESA = 2
    ROLE_CHOICES = (
        (CLIENTE, 'Cliente'),
        (EMPRESA, 'Empresa'),
    )
    email = forms.CharField(label='Email', max_length=60)
    name = forms.CharField(label='Nome', max_length=60)
    address = forms.CharField(label='Endereço', max_length=50)
    city = forms.CharField(label='Cidade', max_length=60)
    state_province = forms.CharField(label='Estado', max_length=2)
    country = forms.CharField(label='', max_length=50)
    cnpj_cpf = forms.CharField(label='', max_length=14)
    category = forms.CharField(label='Categoria')
    is_customer = forms.RadioSelect(choices=ROLE_CHOICES)

    class Meta:
        model = Customer
        fields = ('name', 'email', 'city', 'password2')
