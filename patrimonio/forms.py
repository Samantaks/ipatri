from django import forms
from .models import Depreciacao, Item, Contacontabil,Estado
from usuario.models import Setor


class ItensCadastroForm(forms.Form):
    @staticmethod
    def get_contacontabil_queryset():
        return Contacontabil.objects.all()

    @staticmethod
    def get_depreciacao_queryset():
        return Depreciacao.objects.all()

    @staticmethod
    def get_estado_queryset():
        return Estado.objects.all()

    @staticmethod
    def get_setor_queryset():
        return Setor.objects.all()

    ItemTombo = forms.CharField(
        label="Tombo:",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o tombo do item'})
    )
    ItemNome = forms.CharField(
        label="Nome:",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do item'})
    )
    ItemDescricao = forms.CharField(
        label="Descrição:",
        widget=forms.Textarea(attrs={'placeholder': 'Descreva o item'}),
        required=False
    )

    ItemEstado = forms.ModelChoiceField(
        label="Estado do patrimônio:",
        queryset=get_estado_queryset(),
        empty_label="...",
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Selecione o estado'})
    )

    ItemMarca = forms.CharField(
        label="Marca:",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Digite a marca do item'})
    )
    ItemAno = forms.IntegerField(
        label="Ano:",
        widget=forms.NumberInput(attrs={'placeholder': 'Digite o ano de fabricação'})
    )
    ItemPreco = forms.DecimalField(
        label="Preço:",
        max_digits=20,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Digite o preço do item'})
    )
    ItemData = forms.DateField(
        label="Data:",
        widget=forms.DateInput(attrs={
            'type': 'date'
        })
    )
    ItemNotaFiscal = forms.IntegerField(
        label="NF:",
        widget=forms.NumberInput(attrs={'placeholder': 'Digite o número da nota fiscal'})
    )

    ItemSetor = forms.ModelChoiceField(
        label="Setor de Origem do patrimônio:",
        queryset=get_setor_queryset(),
        empty_label="...",
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Selecione o setor'})
    )

    ItemDepreciacao = forms.ModelChoiceField(
        label="Tipo de Depreciação",
        queryset=get_depreciacao_queryset(),
        empty_label="...",
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Selecione a depreciação'})
    )
    ItemCC = forms.ModelChoiceField(
        label="Tipo de Conta Contabil:",
        queryset=get_contacontabil_queryset(),
        empty_label="...",
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Selecione a conta contábil'})
    )



class ItemSearchForm(forms.Form):
    tombo = forms.IntegerField(label='Tombo', required=True)


class EditItemSetorForm(forms.ModelForm):
    dataalocacao = forms.DateTimeField(
        label='Data e Hora da Movimentação',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        required=True
    )

    estado = forms.CharField(
        label='Estado do item',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Item
        fields = ['setor_id_setor', 'dataalocacao', 'estado']  # Inclui o campo estado
        labels = {
            'setor_id_setor': 'Novo Setor',
            'dataalocacao': 'Data e Hora da Movimentação',
            'estado': 'Estado',
        }
        widgets = {
            'setor_id_setor': forms.Select(attrs={'class': 'form-control'}),
        }
