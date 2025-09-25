from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Campus, Curso, Status, TipoSolicitacao, Servidor, Aluno, Solicitacao, Historico

# View para controle de autenticação e acesso às páginas
from django.contrib.auth.mixins import LoginRequiredMixin

# Importação das coisas do Django Filter
from django_filters.views import FilterView # usada no lugar da ListView
from .filters import HistoricoFilter, HistoricoFilter2 # O filtro criado no filters.py

# Create your views here.
class CampusCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Campus
    success_url = reverse_lazy("listar-campus")
    fields = ["nome"]
    extra_context = {
        "titulo" : "Cadastro de Campus"
    }        


class CursoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Curso
    success_url = reverse_lazy("listar-curso")
    fields = ["nome", "campus"]
    extra_context = {
        "titulo" : "Cadastro de Curso"
    }


class StatusCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Status
    success_url = reverse_lazy("listar-status")
    fields = ["nome", "ordem", "pode_editar"]
    extra_context = {
        "titulo" : "Cadastro de Status"
    }


class TipoSolicitacaoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = TipoSolicitacao
    success_url = reverse_lazy("listar-tipo-solicitacao")
    fields = [
        "descricao",
        "prazo_externo",
        "prazo_externo_dias",
        "prazo_interno",
        "prazo_interno_dias",
    ]
    extra_context = {
        "titulo": "Cadastro de Tipo de Solicitação"
    }


class ServidorCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Servidor
    success_url = reverse_lazy("listar-servidor")
    fields = ["nome", "siape", "campus"]
    extra_context = {
        "titulo": "Cadastro de Servidor"
    }


class AlunoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Aluno
    success_url = reverse_lazy("listar-aluno")
    fields = ["nome", "matricula", "campus", "cpf", "telefone"]
    extra_context = {
        "titulo": "Cadastro de Aluno"
    }


class SolicitacaoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Solicitacao
    success_url = reverse_lazy("listar-solicitacao")
    fields = ["curso", "turma", "tipo_solicitacao", "justificativa", "anexo"]
    extra_context = {
        "titulo": "Cadastro de Solicitação"
    } 

    # Manipular os dados que serão utilizardos para montar o formulário
    # Isso deve ser feito no Create e no Update também
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Fazer um select_related no curso porque ele exibe o campus no __str__ (toString dele)
        qs = Curso.objects.all().select_related("campus")
        # Poderíamos filtrar os cursos pelo campus do usuário logado
        # Verifica se o User é aluno ou servidor e busca seu campus
        if(hasattr(self.request.user, "aluno")):
            qs = qs.filter(campus=self.request.user.aluno.campus)
        elif(hasattr(self.request.user, "servidor")):
            qs = qs.filter(campus=self.request.user.servidor.campus)
        form.fields["curso"].queryset = qs
        return form

    # Método que é executado quando o formulário é válido e vai ser salvo no banco
    def form_valid(self, form):    

        # Verifica se o usuário é um aluno
        if(not hasattr(self.request.user, "aluno")):
            form.add_error("", "Apenas alunos podem fazer solicitações!")
            return self.form_invalid(form)
        
        # Define o usuário logado no "campo do form" (como atributo)
        form.instance.solicitado_por = self.request.user.aluno

        # Manipula os dados do formulário ou que serão salvos no banco
        # Sempre manipulando: form.instance.atributo

        # Executa as validações, faz insert no banco e cria o objeto
        # retorna um redirecionamento para a página de sucesso 
        url = super().form_valid(form)

        # Agora já podemos acessar o objeto do tipo dessa classe (Solicitação)
        # O objeto criado está disponível em: self.object

        # Na minha regra de negócio, preciso criar um histórico pra essa solicitação

        # Tratamento de erro para evitar que alguma solicitação fique cadastrada sem histórico
        try:
            # Busca o objeto status que tem a ordem igual a 1
            status_aberto = Status.objects.get(ordem=1)
            # Cria um objeto solicitação (que é inserido no banco ao criar o objeto)
            historico = Historico.objects.create(
                solicitacao=self.object,
                status=status_aberto,
                gerado_por=self.request.user
            )
        except :
            # Caso de algum erro, deleta a solicitação que foi criada
            self.object.delete()
            # Adiciona um erro ao formulário
            form.add_error("", "Houve um problema, tente novamente!")
            # Retorna ao formulário com o erro adicionado
            return self.form_invalid(form)

        # Se prcisar alterar algum atributo do objeto, deve salvar o objeto para que seja feito um Update no banco
        # self.object.justificativa += "XXXX"
        # Salvar o objeto
        # self.object.save()

        # Se tudo deu certo, retorna o redirecionamento de sucesso
        return url
    



class HistoricoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Historico
    success_url = reverse_lazy("listar-historico")
    fields = ["solicitacao", "status"]
    extra_context = {
        "titulo": "Movimentação de Solicitação",
        "botao" : "Movimentar Solicitação"
    }

    # Identifica o usuário logado e atribui ao campo "gerado_por"
    def form_valid(self, form):
        form.instance.gerado_por = self.request.user
        return super().form_valid(form)


###############################################################


class CampusUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Campus
    success_url = reverse_lazy("listar-campus")
    fields = ["nome"]
    extra_context = {
        "titulo" : "Atualizar dados do Campus"
    } 


class CursoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Curso
    success_url = reverse_lazy("listar-curso")
    fields = ["nome", "campus"]
    extra_context = {
        "titulo" : "Atualização de Curso"
    }


class StatusUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Status
    success_url = reverse_lazy("listar-status")
    fields = ["nome", "ordem", "pode_editar"]
    extra_context = {
        "titulo" : "Atualização de Status"
    }


class TipoSolicitacaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = TipoSolicitacao
    success_url = reverse_lazy("listar-tipo-solicitacao")
    fields = [
        "descricao",
        "prazo_externo",
        "prazo_externo_dias",
        "prazo_interno",
        "prazo_interno_dias",
    ]
    extra_context = {
        "titulo": "Atualização de Tipo de Solicitação"
    }


class ServidorUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Servidor
    success_url = reverse_lazy("listar-servidor")
    fields = ["nome", "siape", "campus"]
    extra_context = {
        "titulo": "Atualização de Servidor"
    }


class AlunoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Aluno
    success_url = reverse_lazy("listar-aluno")
    fields = ["nome", "matricula", "campus", "cpf", "telefone"]
    extra_context = {
        "titulo": "Atualização de Aluno"
    }


class SolicitacaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Solicitacao
    success_url = reverse_lazy("listar-solicitacao")
    fields = ["curso", "turma", "tipo_solicitacao", "justificativa", "anexo"]
    extra_context = {
        "titulo": "Atualização de Solicitação"
    }

    # Manipular os dados que serão utilizardos para montar o formulário
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Fazer um select_related no curso porque ele exibe o campus no __str__ (toString dele)
        form.fields["curso"].queryset = Curso.objects.all().select_related("campus")
        return form

    # Personaliza a busca do objeto que será editado
    def get_object(self):

        # Busca o último histórico da solicitação
        historico = Historico.objects.filter(
            solicitacao__pk=self.kwargs["pk"]).order_by("-id").first()

        # Se o status da solicitação não permite edição, não deixa editar
        if(not historico.status.pode_editar):
            # Força um erro 404 (não encontrado)
            raise Http404("Essa solicitação não pode ser editada!")

        # Se o usuário pertence ao grupo "Admin" pode buscar só pelo ID
        if(self.request.user.groups.filter(name="Admin").exists()):
            return get_object_or_404(Solicitacao, pk=self.kwargs["pk"])
        # Senão, só pode buscar se for o dono da solicitação
        else:
            return get_object_or_404(Solicitacao, pk=self.kwargs["pk"], solicitado_por=self.request.user.aluno)


class HistoricoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Historico
    success_url = reverse_lazy("listar-historico")
    fields = ["solicitacao", "status", "gerado_por"]
    extra_context = {
        "titulo": "Atualização de Histórico"
    }


###############################################################


class CampusDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Campus
    success_url = reverse_lazy("listar-campus")
    extra_context = {
        "titulo" : "Excluir Campus",
    }


class CursoDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Curso
    success_url = reverse_lazy("listar-curso")
    extra_context = {
        "titulo" : "Excluir Curso",
    }


class StatusDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Status
    success_url = reverse_lazy("listar-status")
    extra_context = {
        "titulo" : "Excluir Status",
    }


class TipoSolicitacaoDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = TipoSolicitacao
    success_url = reverse_lazy("listar-tipo-solicitacao")
    extra_context = {
        "titulo" : "Excluir Tipo de Solicitação",
    }

    def get_object(self):
        return get_object_or_404(Solicitacao, pk=self.kwargs["pk"], solicitado_por=self.request.user.aluno)


class ServidorDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Servidor
    success_url = reverse_lazy("listar-servidor")
    extra_context = {
        "titulo" : "Excluir Servidor",
    }


class AlunoDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Aluno
    success_url = reverse_lazy("listar-aluno")
    extra_context = {
        "titulo" : "Excluir Aluno",
    }


class SolicitacaoDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Solicitacao
    success_url = reverse_lazy("listar-solicitacao")
    extra_context = {
        "titulo" : "Excluir Solicitação",
    }


class HistoricoDelete(LoginRequiredMixin, DeleteView):
    template_name = "protocolos/form-excluir.html"
    model = Historico
    success_url = reverse_lazy("listar-historico")
    extra_context = {
        "titulo" : "Excluir Histórico",
    }


###############################################################


class CampusList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/campus.html"
    model = Campus


class CursoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/curso.html"
    model = Curso
    ordering = ["campus", "nome"]

    # Alterar o método de consulta (queryset) para fazer o select related (join no SQL)
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("campus")


class StatusList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/status.html"
    model = Status
    ordering = ["ordem"]


class TipoSolicitacaoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/tipo-solicitacao.html"
    model = TipoSolicitacao


class ServidorList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/servidor.html"
    model = Servidor

    # Alterar o método de consulta (queryset) para fazer o select related (join no SQL)
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("usuario")


class AlunoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/aluno.html"
    model = Aluno

    # Alterar o método de consulta (queryset) para fazer o select related (join no SQL)
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("usuario")

class SolicitacaoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/solicitacao.html"
    model = Solicitacao

    # Alterar o método de consulta (queryset) para fazer o select related (join no SQL)
    def get_queryset(self):
        qs = super().get_queryset()

        # Recebe o valor vindo por GET pelo "name" do input/select
        termo_busca = self.request.GET.get("termo_busca")

        # import o Q para fazer buscas com "ou" (OR)
        from django.db.models import Q

        # Se existir algum dado lá
        if(termo_busca):
            qs = qs.filter(
                Q(solicitado_por__nome__icontains=termo_busca) |
                Q(curso__nome__icontains=termo_busca) |
                Q(tipo_solicitacao__descricao__icontains=termo_busca) |
                Q(curso__campus__nome__icontains=termo_busca)
            )

        # Recebe a data do form de filtro
        data_solicitacao = self.request.GET.get("data_solicitacao")
        if(data_solicitacao):
            # __lte significa menor que ou igual a
            # __gte >=
            # __date verifica só a data, sem hora, minuto ou segundo
            qs = qs.filter(solicitado_em__lte=data_solicitacao)

            
        return qs.select_related("solicitado_por", "curso", "tipo_solicitacao")


class MinhaSolicitacaoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/solicitacao.html"
    model = Solicitacao

    # Alterar o método de consulta (queryset) para fazer o select related (join no SQL)
    def get_queryset(self):
        qs = super().get_queryset().filter(solicitado_por=self.request.user.aluno)
        return qs.select_related("solicitado_por", "curso", "tipo_solicitacao")


class HistoricoList(LoginRequiredMixin, FilterView):
    template_name = "protocolos/listas/historico.html"
    model = Historico
    filterset_class = HistoricoFilter2

    # Alterar o método de consulta (queryset) para fazer o select related (join no SQL)
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("solicitacao", "status", "gerado_por", "solicitacao__tipo_solicitacao")
