from django.contrib.auth.models import User
from django.db import models
from utils.lists import CUSTOMER_TYPE, IS_CUSTOMER


class CategoriaProduto(models.Model):
    """ Class Category - This class to save data from category."""
    nome = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nome

    def get_fields(self):
        return [(field, field.value_to_string(self)) for field in CategoriaProduto._meta.fields]


class Vendedor(User):
    ''' Vendedor.'''
    razaosocial = models.CharField(max_length=50, null=True)
    endereco = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=True, blank=True)
    estado = models.CharField(max_length=30, null=True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14,
                            unique=True, null=True, blank=True)
    ie = models.CharField(u'inscrição estadual',
                          max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return str(self.razaosocial)


class Comprador(User):
    ''' Comprador.'''
    nome = models.CharField(max_length=50, null=True)
    endereco = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=True, blank=True)
    estado = models.CharField(max_length=30, null=True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11,
                           unique=True, null=True, blank=True)
    rg = models.CharField('RG', max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = 'comprador'
        verbose_name_plural = 'compradores'

    def __str__(self):
        return str(self.email)


class EventoCompra(models.Model):
    """Evento de Compra de Produto."""
    nomeproduto = models.CharField(max_length=50, null=False)
    descricao = models.TextField(blank=True)
    comprador = models.ForeignKey(Comprador, null=True)
    categoriaproduto = models.ForeignKey(CategoriaProduto, null=True)
    preco = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    facebook_likes = models.IntegerField(default=0)
    imagemproduto = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'eventocompra'
        verbose_name_plural = 'eventoscompras'

    def __str__(self):
        return self.nomeproduto















