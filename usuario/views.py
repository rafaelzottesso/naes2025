from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from protocolos.models import Aluno, Servidor
from .forms import UsuarioCadastroForm


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'protocolos/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários'}


    def form_valid(self, form):
        
        # Pega os dados do form, antes de criar o objeto
        nome = form.cleaned_data['nome']
        cpf = form.cleaned_data['cpf']
        identificacao = form.cleaned_data['identificacao']
        tipo = form.cleaned_data['tipo_usuario']

        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        
        # Usa um try para não correr o risco de cadastrar o usuário
        # e acontecer um erro durante o cadastro de Aluno ou Servidor
        # e o User ficar sem relação "travando" o uso daqueles dados
        try:

            if(tipo == "Estudante"):
                # Criar um objeto aluno para este usuário
                aluno = Aluno.objects.create(
                    nome = nome,            
                    cpf = cpf,
                    matricula = identificacao,            
                    usuario = self.object,
                )
                # Busca ou cria um grupo com esse nome
                grupo, criado = Group.objects.get_or_create(name='Estudante')
                # Acessa o objeto criado e adiciona o usuário no grupo acima
                self.object.groups.add(grupo)

            else:
                servidor = Servidor.objects.create(
                    nome = nome,            
                    siape = identificacao,            
                    usuario = self.object,
                )
                # Busca ou cria um grupo com esse nome
                grupo, criado = Group.objects.get_or_create(name='Servidor')
                # Acessa o objeto criado e adiciona o usuário no grupo acima
                self.object.groups.add(grupo)

        # Caso de algum problema na criação de Aluno ou Servidor
        except:
            # Exclui o user pra liberar os dados dele
            self.object.delete()
            # Retorna um erro no formulário
            form.add_error("", "Houve um problema para criar o aluno, tente novamente!")
            # Retorna ao formulário com o erro adicionado
            return self.form_invalid(form)

        # Retorna a URL de sucesso
        return url
