from django.db import models
from core.models import EventoCompra


class Situacao(models.Model):
    descricao = models.CharField(max_length=30, null=True, blank=True)


class Meta:
    verbose_name = 'situacao'
    verbose_name_plural = 'situacao'


def __str__(self):
    return self.descricao


class Propostas(models.Model):
    """Proposta de Compra de produto."""
    anuncio = models.ForeignKey(EventoCompra, null=False)
    situacao = models.ForeignKey(Situacao, null=True)
    valorofertado = models.DecimalField(max_digits=19, decimal_places=2, blank=True)

    class Meta:
        verbose_name = 'proposta'
        verbose_name_plural = 'propostas'

    def __str__(self):
        return self.anuncio
