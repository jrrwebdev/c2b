from django import forms
from django.core.exceptions import ValidationError
from propostas.models import Propostas


class PropostaForm(forms.Form):
    class Meta:
        model = Propostas
        fields = ('anuncio',
                  'situacao',
                  'valorofertado')


        labels = {
            'anuncio': ('anuncio'),
            'situacao': ('Situação'),
            'valorofertado': ('Valor Oferta'),
        }
