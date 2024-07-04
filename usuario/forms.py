from django import forms

SECRETARIA_CHOICES = (
    ('Seplan', 'Secretária de Estado do Planejamento e Orçamento'),
    ('CC', 'Casa Civil')
)


class LoginForm(forms.Form):
    cpf = forms.CharField(max_length=20)
    senha = forms.CharField(widget=forms.PasswordInput())


class CadastroForm(forms.ModelForm):
    fname = forms.CharField(max_length=120)
    lname = forms.CharField(max_length=120)
    Email = forms.EmailField(max_length=200)
    ConfEmail = forms.CharField(max_length=200)
    cpf = forms.CharField(max_length=20)
    senha = forms.CharField(widget=forms.PasswordInput())
    secretaria = forms.ChoiceField(choices=SECRETARIA_CHOICES)
