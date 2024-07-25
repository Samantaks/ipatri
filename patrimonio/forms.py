from django import forms


class ItensCadastroForm(forms.Form):
    ItemNome = forms.CharField(label="Nome:", max_length=200)
    ItemTombo = forms.CharField(label="Tombo:", max_length=200)
    ItemMarca = forms.CharField(label="Marca:", max_length=200)
    ItemPreco = forms.CharField(label="Preço:", max_length=200)
    ItemAno = forms.CharField(label="Ano:", max_length=200)
    ItemNotaFiscal = forms.CharField(label="Nota Fiscal:", max_length=200)
