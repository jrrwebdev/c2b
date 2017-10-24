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


class BuyEvent(models.Model):
    """Class Buy Event - This class is to save data from Buy Events."""
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    like = models.IntegerField(default=0)
    photo = models.ImageField(blank=True)


    def __str__(self):
        return self.name



class Customer(User):
    ''' Class Customer - This class to save data from customer.'''
    category = models.ForeignKey("Category", blank=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    cpf = models.CharField('CPF', max_length=11,
                           unique=True, null=True, blank=True)
    rg = models.CharField('RG', max_length=11, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14,
                            unique=True, null=True, blank=True)
    ie = models.CharField(u'inscrição estadual',
                          max_length=12, null=True, blank=True)
    person_type = models.CharField(
        'Fisica ou Juridica', max_length=1, choices=CUSTOMER_TYPE, default='F')
    is_customer = models.CharField(
        'tipo de cliente', max_length=1, choices=IS_CUSTOMER, blank=True)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.username
