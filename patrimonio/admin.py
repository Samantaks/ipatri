from django.contrib import admin
from .models import Item, Depreciacao, Contacontabil,Estado


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('idpatrimonio', 'tombo', 'itemnome', 'descricao', 'datacompra', 'itemano',
                    'marca', 'valorcompra', 'notafiscal', 'setor_id_setor')


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('idestado', 'tipoestado', 'descricaoestado')


admin.site.register(Item, ItemAdmin)
admin.site.register(Depreciacao)
admin.site.register(Contacontabil)
admin.site.register(Estado, EstadoAdmin)
