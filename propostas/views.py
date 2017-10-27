from django.conf import settings
# from django.contrib import messages
from django.core import mail
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from propostas.forms import PropostaForm
from propostas.models import Propostas

def propostas(request):
    return render(request)

def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'proposta_form.html', {'form': PropostaForm()})


def create(request):
    form = PropostaForm(request.POST)
    if not form.is_valid():
        return render(request, 'proposta_form.html', {'form': form})

    Proposta = Propostas.objects.create(**form.cleaned_data)
    _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, Proposta.email,
               'propostas/Proposta_email.txt', {'proposta': Proposta})


    # messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect(r('propostas:detail', Proposta.pk))


def detail(request, pk):
    try:
        Proposta = Propostas.objects.get(pk=pk)
    except Proposta.DoesNotExist:
        raise Http404
    return render(request, 'propostas/proposta_detail.html', {'proposta': Proposta})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
