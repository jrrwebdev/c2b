from django.contrib import admin
from core.models import Saler, Buyer, BuyEvent, Category

class BuyEventAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('name', 'description', 'category', 'price', 'like', 'photo')

class BuyerAdmin(admin.ModelAdmin):
    ''' Comprador.'''
    fields = ('username',  'first_name', 'last_name', 'address', 'city', 'state_province', 'country' , 'cpf', 'rg')

class SalerAdmin(admin.ModelAdmin):
    ''' Vendedor.'''
    fields = ('username',  'razaosocial', 'address', 'city', 'state_province', 'country' , 'cnpj', 'ie')

admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Saler, SalerAdmin)
admin.site.register(BuyEvent, BuyEventAdmin)
admin.site.register(Category)
