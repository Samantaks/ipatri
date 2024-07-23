from django.contrib import admin
from .models import Usuario, Setor
# from .forms import UsuarioForm, SetorForm


class UsuarioAdmin(admin.ModelAdmin):
   # form = UsuarioForm
    list_display = ('idusuario', 'nomeusuario', 'sobrenome',
                    'email', 'cpf', 'get_setor_nome')

    def formfield(self, request, field_name, **kwargs):
        if field_name == 'setor_id_setor':
            kwargs['widget'] = admin.widgets.Select(
                choices=Usuario.objects.values_list('setor_id_setor', 'setor__nome'))
        return super().formfield(request, field_name, **kwargs)

    def get_setor_nome(self, obj):
        return obj.setor_id_setor.setor_abrev
    get_setor_nome.short_description = 'Setor'


class SetorAdmin(admin.ModelAdmin):

    list_display = ('id_setor', 'setor_abrev',
                    'setor_full', 'orgao_abrev')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Setor, SetorAdmin)
