import datetime
from django import forms
from .models import *


class ItensCadastroForm(forms.Form):
    ItemTombo = forms.CharField(label="Tombo:", max_length=200)
    ItemNome = forms.CharField(label="Nome:", max_length=200)
    ItemDescricao = forms.CharField(label="Descrição do Item:", widget=forms.Textarea, required=False)
    ItemMarca = forms.CharField(label="Marca:", max_length=200)
    ItemAno = forms.IntegerField(label="Ano do Item:")
    ItemPreco = forms.DecimalField(label="Preço do item foi...", max_digits=20, decimal_places=2)
    ItemData = forms.DateField(label="Data de Compra:", widget=forms.DateInput(attrs={'type': 'date'}))
    ItemNotaFiscal = forms.IntegerField(label="Nota Fiscal:")
    #ItemDepreciacao = forms.ModelChoiceField(queryset=Item.depreciacao_iddepreciacao1.objects.all(),
    #                                     empty_label="Selecione um item", required=True, widget=forms.Select)
    #ItemSecretaria = forms.ModelChoiceField(queryset=Item.setor_id_setor.objects.all(),
    #                                     empty_label="Selecione um item", required=True, widget=forms.Select)
