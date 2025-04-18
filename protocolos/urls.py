from django.urls import path

# Importar suas views
from .views import (
    CampusCreate,
    CursoCreate,
    StatusCreate,
    TipoSolicitacaoCreate,
    ServidorCreate,
    AlunoCreate,
    SolicitacaoCreate,
    HistoricoCreate,
)

urlpatterns = [
    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),
    path("cadastrar/curso/", CursoCreate.as_view(), name="cadastrar-curso"),
    path("cadastrar/status/", StatusCreate.as_view(), name="cadastrar-status"),
    path("cadastrar/tipo-solicitacao/", TipoSolicitacaoCreate.as_view(), name="cadastrar-tipo-solicitacao"),
    path("cadastrar/servidor/", ServidorCreate.as_view(), name="cadastrar-servidor"),
    path("cadastrar/aluno/", AlunoCreate.as_view(), name="cadastrar-aluno"),
    path("cadastrar/solicitacao/", SolicitacaoCreate.as_view(), name="cadastrar-solicitacao"),
    path("cadastrar/historico/", HistoricoCreate.as_view(), name="cadastrar-historico"),
]