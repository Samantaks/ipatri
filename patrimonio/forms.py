import datetime
from django import forms


class ItensCadastroForm(forms.Form):
    ItemTombo = forms.CharField(label="Tombo:", max_length=200)
    ItemNome = forms.CharField(label="Nome:", max_length=200)
    ItemDescricao = forms.Textarea()
    ItemMarca = forms.CharField(label="Marca:", max_length=200)
    ItemAno = forms.IntegerField(label="Ano do Item:")
    ItemPreco = forms.DecimalField(label="Preço do item foi...", max_digits=20, decimal_places=2)
    ItemData = forms.DateField(label="Data de Compra:", widget=forms.DateInput(attrs={'type': 'date'}))
    ItemNotaFiscal = forms.CharField(label="Nota Fiscal:", max_length=200)
