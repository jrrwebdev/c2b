# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse

from django.views.generic import CreateView

from core.forms import RegisterCustomerForm


def home(request):
    return render(request, "index.html")


class RegisterCustomerView(CreateView):
    form_class = RegisterCustomerForm
    template_name = "core/register_customer.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterCustomerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return HttpResponse('User registered')


