from django.shortcuts import render

# View que apenas renderiza uma página Web
from django.views.generic import TemplateView

from protocolos.models import Solicitacao, Aluno, Servidor

# Create your views here.

# Cria uma view para renderizar a página inicial
# e faz uma herança de TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Enviando uma str básica
        context["nome"] = "Rafael Zottesso"
        # Enviar uma lista de objetos
        context["ultimas"] = Solicitacao.objects.all().order_by('-solicitado_em')[:5]
        context["qtde"] = Solicitacao.objects.all().count()
        context["qtde_alunos"] = Aluno.objects.all().count()
        context["qtde_servidores"] = Servidor.objects.all().count()
        return context


class SobreView(TemplateView):
    template_name = "paginasweb/sobre.html"


class ContatoView(TemplateView):
    template_name = "paginasweb/contato.html"