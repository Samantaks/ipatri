from django import forms

SECRETARIA_CHOICES = (
    ('', 'Escolha entre...'),
    ('Seplan', 'Secretária de Estado do Planejamento e Orçamento'),
    ('CC', 'Casa Civil')
)


class LoginForm(forms.Form):
    cpf = forms.CharField(label="CPF:", max_length=20)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput())


class CadastroForm(forms.Form):
    fname = forms.CharField(label="Nome:", max_length=200)
    lname = forms.CharField(label="Sobrenome:", max_length=200)
    Email = forms.EmailField(label="Email:", max_length=200)
    ConfEmail = forms.CharField(label="Confirme o seu Email:", max_length=200)
    cpf = forms.CharField(label="CPF:", max_length=20)
    senha = forms.CharField(label="Senha:", widget=forms.PasswordInput())
    ConfSenha = forms.CharField(label="Confirme sua Senha:", widget=forms.PasswordInput())
    secretaria = forms.ChoiceField(label="Escolha uma secretaria", choices=SECRETARIA_CHOICES)