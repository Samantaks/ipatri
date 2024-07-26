from django.contrib import admin
from .models import Item, Depreciacao, Contacontabil
from usuario.models import Setor


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('idpatrimonio', 'tombo', 'itemnome', 'descricao', 'datacompra', 'itemano',
                    'marca', 'valorcompra', 'notafiscal', 'setor_id_setor')

    def formfield(self, request, field_name, **kwargs):
        if field_name == 'setor_id_setor':
            kwargs['widget'] = admin.widgets.Select(
                choices=Item.objects.values_list('setor_id_setor', 'setor__nome'))
        return super().formfield(request, field_name, **kwargs)

    def get_setor_nome(self, obj):
        return obj.setor_id_setor.setor_abrev
    get_setor_nome.short_description = 'Setor'


admin.site.register(Item, ItemAdmin)
admin.site.register(Depreciacao)
admin.site.register(Contacontabil)
