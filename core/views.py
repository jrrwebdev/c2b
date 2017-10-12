from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomerForm


def home(request):
    boards = "Contexto"
    return render(request, 'home.html', {'boards': boards})


def customer_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()

    return render(request, 'customer_add.html', {'form': form})
