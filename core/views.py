from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy

from core import forms
from core.forms import BuyerForm, SalerForm, AnunciarForm
from core.models import BuyEvent


def home(request):
    meusanuncios = BuyEvent.objects.all()
    return render(request, 'home.html', {'anuncios': meusanuncios})

def meusanuncios(request):
    meusanuncios = BuyEvent.objects.all()
    return render(request, 'anuncios.html', {'anuncios': meusanuncios})


def novousuario(request):
    return render(request, 'novousuario.html')


def signupvendedor(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SalerForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            messages.success(request, 'Usuario Adicionado com Sucesso')
            return HttpResponseRedirect(reverse_lazy('sucesso'))
    else:
        form = SalerForm()
    context = {'form': form}
    return render(request, 'signupvendedor.html', {'form': form}, context)


def signupcomprador(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            messages.success(request, 'Usuario Adicionado com Sucesso')
            return HttpResponseRedirect(reverse_lazy('sucesso'))
    else:
        form = BuyerForm()
    context = {'form': form}
    return render(request, 'signupcomprador.html', {'form': form}, context)


# @login_required
def customer_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SalerForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            messages.success(request, 'Usuario Adicionado com Sucesso')
            return HttpResponseRedirect(reverse_lazy('sucesso'))
    else:
        form = SalerForm()
    context = {'form': form}
    return render(request, 'customer.html', {'form': form}, context)


@login_required
def anunciar(request):
    if request.method == 'POST':
        form = forms.AnunciarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anuncio Cadastrado com Sucesso')
            return HttpResponseRedirect(reverse_lazy('sucesso'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.AnunciarForm()
    context = {'form': form}
    return render(request, 'anunciar.html', {'form': form}, context)

