from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from protocolos.models import Aluno, Servidor, Campus
from django import forms


# Crie uma classe de formulário para o cadastro de usuários
# A herança é feita para poder tornar o email único e obrigatório
# E outros campos, se necessário
class UsuarioCadastroForm(UserCreationForm):

    TIPOS = [
        ("Estudante", "Estudante"),
        ("Servidor", "Servidor")
    ]

    nome = forms.CharField(required=True, max_length=255)
    cpf = forms.CharField(required=True, max_length=14, label="CPF")

    identificacao = forms.CharField(required=True, max_length=50, label="Identificação",
        help_text="Informe a matrícula para Estudante ou SIAPE para Servidor.")
    
    campus = forms.ModelChoiceField(queryset=Campus.objects.all(), required=True, label="Campus",
        help_text="Selecione o campus ao qual você está vinculado.")

    tipo_usuario = forms.ChoiceField(choices=TIPOS, label="Tipo de usuário")

    email = forms.EmailField(required=True, help_text="Informe um email válido.")

    # Define o model e os fields que vão aparecer na tela
    class Meta:
        model = User
        # Esses dois passwords são para verificar se as senhas são iguais
        fields = [ 'nome', 'tipo_usuario', 'identificacao', 'campus',
                    'cpf', 'username', 'email',
                    'password1', 'password2' ]

    # O metodo clean no forms serve de validação para os campos
    def clean_email(self):
        # recebe o email do formulário
        email = self.cleaned_data.get('email')
        # Verifica se já existe algum usuário com este email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean_identificacao(self):
        doc = self.cleaned_data.get('identificacao')

        if self.cleaned_data.get('tipo_usuario') == "Estudante":
            if Aluno.objects.filter(matricula=doc).exists():
                raise forms.ValidationError("Esta matrícula já está em uso.")
        else:
            if Servidor.objects.filter(siape=doc).exists():
                raise forms.ValidationError("Este Siape já está em uso.")
        
        return doc

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Aluno.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está em uso.")
        return cpf
