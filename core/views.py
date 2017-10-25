from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import CustomerForm, AnunciarForm
from .models import BuyEvent, Customer


def home(request):
    meusanuncios = BuyEvent.objects.all()
    customercontext = Customer.objects.all()
    print("Cust", customercontext)
    return render(request, 'home.html', {'anuncios': meusanuncios}, {'customer': customercontext})

def meusanuncios(request):
    meusanuncios = BuyEvent.objects.all()
    return render(request, 'anuncios.html', {'anuncios': meusanuncios})


# @login_required
def customer_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            messages.success(request, 'Usuario Adicionado com Sucesso')
            return HttpResponseRedirect(reverse_lazy('sucesso'))
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
            return HttpResponseRedirect(reverse_lazy('sucesso'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnunciarForm()
    context = {'form': form}
    return render(request, 'anunciar.html', {'form': form}, context)





def LikeBuyEvent(request):
    anuncios = BuyEvent.objects.all()
    return render(request, 'anuncios.html', {'anuncios': anuncios})