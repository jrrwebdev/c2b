from django.contrib import admin
from core.models import Vendedor, Comprador, EventoCompra, CategoriaProduto

class EventoCompraAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('nomeproduto', 'comprador', 'descricao', 'categoriaproduto', 'preco', 'facebook_likes', 'imagemproduto')

class CompradorAdmin(admin.ModelAdmin):
    ''' Comprador.'''
    fields = ('username', 'nome',  'email', 'first_name', 'last_name', 'endereco', 'cidade', 'estado', 'pais' , 'cpf', 'rg')

class VendedorAdmin(admin.ModelAdmin):
    ''' Vendedor.'''
    fields = ('username', 'razaosocial', 'email', 'endereco', 'cidade', 'estado', 'pais' , 'cnpj', 'ie')

admin.site.register(Comprador, CompradorAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(EventoCompra, EventoCompraAdmin)
admin.site.register(CategoriaProduto)
