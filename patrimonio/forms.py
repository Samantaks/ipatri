import datetime
from django import forms


class ItensCadastroForm(forms.Form):
    ItemTombo = forms.CharField(label="Tombo:", max_length=200)
    ItemNome = forms.CharField(label="Nome:", max_length=200)
    ItemDescricao = forms.Textarea()
    ItemMarca = forms.CharField(label="Marca:", max_length=200)
    ItemAno = forms.CharField(label="Ano do Item:", max_length=200)
    ItemPreco = forms.DecimalField(label="Preço do item foi...", max_digits=20, decimal_places=2)
    ItemData = forms.DateField(initial=datetime.date.today, label="Data de Compra:", widget=forms.DateInput)
    ItemNotaFiscal = forms.CharField(label="Nota Fiscal:", max_length=200)
