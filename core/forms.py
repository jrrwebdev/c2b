from django import forms
from core.models import Customer
from django.core.exceptions import ValidationError




class RegisterCustomerForm(forms.ModelForm):
    CHOICESTYPECUSTOMER = (('C', 'Cliente'),
                           ('E', 'Empresa'))
    is_customer = forms.ChoiceField(label="Você é um?", widget=forms.RadioSelect, choices=CHOICESTYPECUSTOMER)
    name = forms.CharField(max_length=60, label="Nome", widget=forms.TextInput)
    cnpjcpf = forms.CharField(max_length=14, label="CPF", widget=forms.TextInput)
    address = forms.CharField(max_length=50, label="Endereco", widget=forms.TextInput)
    city = forms.CharField(max_length=60, label="Cidade", widget=forms.TextInput)
    state_province = forms.CharField(max_length=30, label="Estado", widget=forms.TextInput)
    country = forms.CharField(max_length=50, label="País", widget=forms.TextInput)
    email = forms.EmailField(label="Email", widget=forms.TextInput)
    if not name and not email:
        raise forms.ValidationError('Something goes wrong, checkout!')


    class Meta:
        model = Customer
        fields = ['is_customer', 'name', 'email']
        widgets = {
            'is_customer': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'name': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True})
        }
