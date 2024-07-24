from django import forms
from .models import Usuario, Setor


class LoginForm(forms.Form):
    cpf = forms.CharField(label="CPF:", max_length=20)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput())


class CadastroForm(forms.Form):
    fname = forms.CharField(label="Nome:", max_length=200)
    lname = forms.CharField(label="Sobrenome:", max_length=200)
    Email = forms.EmailField(label="Email:", max_length=200)
    ConfEmail = forms.CharField(label="Confirme o seu Email:", max_length=200)
    cpf = forms.CharField(label="CPF:", max_length=11)
    senha = forms.CharField(label="Senha:", widget=forms.PasswordInput())
    ConfSenha = forms.CharField(label="Confirme sua Senha:", widget=forms.PasswordInput())


class UsuarioForm(forms.ModelForm):
    setor_nome = forms.CharField(max_length=100, required=False, label='Setor',
                                 widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Usuario
        fields = ['idusuario', 'nomeusuario', 'sobrenome', 'email', 'senha',
                  'cpf', 'setor_id_setor', 'setor_nome']

    def _init_(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['setor_nome'].initial = self.instance.setor_id_setor.setor_abrev


class SetorForm(forms.ModelForm):

    class Meta:
        model = Setor
        fields = ['id_setor', 'setor_abrev', 'orgao_full', 'setor_full', 'orgao_abrev']

    def _init_(self, *args, **kwargs):
        super(SetorForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['id_setor'].initial = self.instance.setor_id_setor
