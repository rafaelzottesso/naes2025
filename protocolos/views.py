from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .models import Campus, Curso, Status, TipoSolicitacao, Servidor, Aluno, Solicitacao, Historico

# Create your views here.
class CampusCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Campus
    success_url = reverse_lazy("index")
    fields = ["nome"]
    extra_context = {
        "titulo" : "Cadastro de Campus"
    }


class CursoCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Curso
    success_url = reverse_lazy("index")
    fields = ["nome", "campus"]
    extra_context = {
        "titulo" : "Cadastro de Curso"
    }


class StatusCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Status
    success_url = reverse_lazy("index")
    fields = ["nome", "ordem", "pode_editar"]
    extra_context = {
        "titulo" : "Cadastro de Status"
    }


class TipoSolicitacaoCreate(CreateView):
    template_name = "protocolos/form.html"
    model = TipoSolicitacao
    success_url = reverse_lazy("index")
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


class ServidorCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Servidor
    success_url = reverse_lazy("index")
    fields = ["nome", "siape", "email"]
    extra_context = {
        "titulo": "Cadastro de Servidor"
    }


class AlunoCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Aluno
    success_url = reverse_lazy("index")
    fields = ["nome", "matricula", "cpf", "email", "telefone"]
    extra_context = {
        "titulo": "Cadastro de Aluno"
    }


class SolicitacaoCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Solicitacao
    success_url = reverse_lazy("index")
    fields = ["solicitado_por", "curso", "turma", "tipo_solicitacao", "justificativa", "anexo"]
    extra_context = {
        "titulo": "Cadastro de Solicitação"
    }


class HistoricoCreate(CreateView):
    template_name = "protocolos/form.html"
    model = Historico
    success_url = reverse_lazy("index")
    fields = ["solicitacao", "status", "gerado_por"]
    extra_context = {
        "titulo": "Cadastro de Histórico"
    }