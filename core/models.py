from django.db import models



class Category(models.Model):
    """ Class Category - This class to save data from category."""
    description = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.description


class BuyEvent(models.Model):
    """Class Buy Event - This class is to save data from Buy Events."""
    description = models.CharField(max_length=50)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    like = models.IntegerField(default=0)
    model_pic = models.ImageField(
        upload_to='pic_folder/', default='img/no-img.jpg')

    def __str__(self):
        return self.description


class Customer(models.Model):
    CLIENTE = 1
    EMPRESA = 2
    ROLE_CHOICES = (
        (CLIENTE, 'Cliente'),
        (EMPRESA, 'Empresa'),
    )
    ''' Class Customer - This class to save data from customer.'''
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)

    cnpj_cpf = models.CharField(max_length=14, null=True)
    category = models.ForeignKey("Category", blank=True)
    is_customer = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)


    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.name
