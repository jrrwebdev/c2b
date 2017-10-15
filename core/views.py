from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomerForm, AnunciarForm
from .models import BuyEvent


def home(request):
    anuncios = BuyEvent.objects.all()
    return render(request, 'home.html', {'anuncios': anuncios})


# @login_required
def customer_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            messages.success(request, 'Usuario Adicionado com Sucesso')
            return HttpResponseRedirect('sucesso.html')
    else:
        form = CustomerForm()
    context = {'form': form}
    return render(request, 'customer.html', {'form': form}, context)


@login_required
def anunciar(request):
    if request.method == 'POST':
        form = AnunciarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anuncio Cadastrado com Sucesso')
            return HttpResponseRedirect('/sucesso/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnunciarForm()
    context = {'form': form}
    return render(request, 'anunciar.html', {'form': form}, context)


def BuyEventsListView(request):
    buyevents = BuyEvent.objects.all()
    return render(request, 'anuncios.html', {'buyevents': buyevents})


def LikeBuyEvent(request):
    anuncios = BuyEvent.objects.all()
    return render(request, 'anuncios.html', {'anuncios': anuncios})