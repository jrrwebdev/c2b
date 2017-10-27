from django.contrib import admin
from propostas.models import Propostas, Situacao


class PropostasAdmin(admin.ModelAdmin):
    fields = ('anuncio', 'situacao', 'valorofertado')



class SituacaoAdmin(admin.ModelAdmin):
    fields = ('descricao',)


admin.site.register(Propostas, PropostasAdmin)
admin.site.register(Situacao, SituacaoAdmin)
