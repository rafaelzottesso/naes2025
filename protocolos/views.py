from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from .models import Campus, Curso, Status, TipoSolicitacao, Servidor, Aluno, Solicitacao, Historico

# View para controle de autenticação e acesso às páginas
from django.contrib.auth.mixins import LoginRequiredMixin


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
    fields = ["nome", "siape", "email"]
    extra_context = {
        "titulo": "Cadastro de Servidor"
    }


class AlunoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Aluno
    success_url = reverse_lazy("listar-aluno")
    fields = ["nome", "matricula", "cpf", "email", "telefone"]
    extra_context = {
        "titulo": "Cadastro de Aluno"
    }


class SolicitacaoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Solicitacao
    success_url = reverse_lazy("listar-solicitacao")
    fields = ["solicitado_por", "curso", "turma", "tipo_solicitacao", "justificativa", "anexo"]
    extra_context = {
        "titulo": "Cadastro de Solicitação"
    }


class HistoricoCreate(LoginRequiredMixin, CreateView):
    template_name = "protocolos/form.html"
    model = Historico
    success_url = reverse_lazy("listar-historico")
    fields = ["solicitacao", "status", "gerado_por"]
    extra_context = {
        "titulo": "Cadastro de Histórico"
    }


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
    fields = ["nome", "siape", "email"]
    extra_context = {
        "titulo": "Atualização de Servidor"
    }


class AlunoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Aluno
    success_url = reverse_lazy("listar-aluno")
    fields = ["nome", "matricula", "cpf", "email", "telefone"]
    extra_context = {
        "titulo": "Atualização de Aluno"
    }


class SolicitacaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "protocolos/form.html"
    model = Solicitacao
    success_url = reverse_lazy("listar-solicitacao")
    fields = ["solicitado_por", "curso", "turma", "tipo_solicitacao", "justificativa", "anexo"]
    extra_context = {
        "titulo": "Atualização de Solicitação"
    }


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


class AlunoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/aluno.html"
    model = Aluno


class SolicitacaoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/solicitacao.html"
    model = Solicitacao


class HistoricoList(LoginRequiredMixin, ListView):
    template_name = "protocolos/listas/historico.html"
    model = Historico
