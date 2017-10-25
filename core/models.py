from django.contrib.auth.models import User
from django.db import models
from utils.lists import CUSTOMER_TYPE, IS_CUSTOMER


class Category(models.Model):
    """ Class Category - This class to save data from category."""
    description = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.description

    def get_fields(self):
        return [(field, field.value_to_string(self)) for field in Category._meta.fields]


class Saler(User):
    ''' Vendedor.'''
    razaosocial = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    cnpj = models.CharField('CNPJ', max_length=14,
                            unique=True, null=True, blank=True)
    ie = models.CharField(u'inscrição estadual',
                          max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return str(self.razaosocial)


class Buyer(User):
    ''' Comprador.'''
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    cpf = models.CharField('CPF', max_length=11,
                           unique=True, null=True, blank=True)
    rg = models.CharField('RG', max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = 'comprador'
        verbose_name_plural = 'compradores'

    def __str__(self):
        return str(self.email)


class BuyEvent(models.Model):
    """Evento de Compra de Produto."""
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    buyerid = models.ForeignKey(Buyer, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    like = models.IntegerField(default=0)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
