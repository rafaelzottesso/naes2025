from django.shortcuts import render
from django.db.models import Count
from datetime import datetime, timedelta

# View que apenas renderiza uma página Web
from django.views.generic import TemplateView

from protocolos.models import Solicitacao, Aluno, Servidor, Status, TipoSolicitacao, Historico

# Create your views here.

# Cria uma view para renderizar a página inicial
# e faz uma herança de TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Enviando uma str básica
        context["nome"] = "Rafael Zottesso"
        
        # Últimas solicitações
        context["ultimas"] = Solicitacao.objects.all().select_related(
            "tipo_solicitacao", "solicitado_por", "curso", "curso__campus"
        ).order_by('-solicitado_em')[:5]
        
        # Estatísticas básicas
        context["qtde"] = Solicitacao.objects.all().count()
        context["qtde_alunos"] = Aluno.objects.all().count()
        context["qtde_servidores"] = Servidor.objects.all().count()
        
        # Estatísticas mais detalhadas
        # Solicitações dos últimos 30 dias
        data_limite = datetime.now() - timedelta(days=30)
        context["qtde_mes"] = Solicitacao.objects.filter(solicitado_em__gte=data_limite).count()
        
        # Tipos de solicitação mais comuns
        context["tipos_mais_comuns"] = TipoSolicitacao.objects.annotate(
            qtde_solicitacoes=Count('solicitacao')
        ).order_by('-qtde_solicitacoes')[:3]
        
        # Solicitações por status (se houver histórico)
        try:
            # Pega o último status de cada solicitação
            context["solicitacoes_por_status"] = Status.objects.annotate(
                qtde=Count('historico__solicitacao', distinct=True)
            ).order_by('ordem')
        except:
            context["solicitacoes_por_status"] = []
        
        return context


class SobreView(TemplateView):
    template_name = "paginasweb/sobre.html"


class ContatoView(TemplateView):
    template_name = "paginasweb/contato.html"