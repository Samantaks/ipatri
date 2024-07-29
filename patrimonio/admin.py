from django.contrib import admin
from .models import Item, Depreciacao, Contacontabil
from usuario.models import Setor


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('idpatrimonio', 'tombo', 'itemnome', 'descricao', 'datacompra', 'itemano',
                    'marca', 'valorcompra', 'notafiscal', 'setor_id_setor')


admin.site.register(Item, ItemAdmin)
admin.site.register(Depreciacao)
admin.site.register(Contacontabil)
