from django import forms
from .models import Depreciacao, Item
from usuario.models import Setor


class ItensCadastroForm(forms.Form):
    @staticmethod
    def get_depreciacao_queryset():
        return Depreciacao.objects.all()

    @staticmethod
    def get_setor_queryset():
        return Setor.objects.all()

    ItemTombo = forms.CharField(label="Tombo:", max_length=200)
    ItemNome = forms.CharField(label="Nome:", max_length=200)
    ItemDescricao = forms.CharField(label="Descrição do Item:", widget=forms.Textarea, required=False)
    ItemMarca = forms.CharField(label="Marca:", max_length=200)
    ItemAno = forms.IntegerField(label="Ano do Item:")
    ItemPreco = forms.DecimalField(label="Preço do item foi...", max_digits=20, decimal_places=2)
    ItemData = forms.DateField(label="Data de Compra:", widget=forms.DateInput(attrs={'type': 'date'}))
    ItemNotaFiscal = forms.IntegerField(label="Nota Fiscal:")
    ItemDepreciacao = forms.ModelChoiceField(
        queryset=get_depreciacao_queryset(),
        empty_label="Selecione um tipo de Depreciação",
        required=True,
        widget=forms.Select
    )

    ItemSetor = forms.ModelChoiceField(
        queryset=get_setor_queryset(),
        empty_label="Selecione o setor do item",
        required=True,
        widget=forms.Select
    )


class ItemSearchForm(forms.Form):
    tombo = forms.IntegerField(label='Tombo', required=True)


class EditItemSetorForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['setor_id_setor']
        widgets = {
            'setor_id_setor': forms.Select(attrs={'class': 'form-control'}),
        }