from django.urls import path

# Importar suas views
from .views import CampusCreate,CursoCreate,StatusCreate,TipoSolicitacaoCreate,ServidorCreate,AlunoCreate,SolicitacaoCreate,HistoricoCreate
from .views import CampusUpdate, CursoUpdate, StatusUpdate, TipoSolicitacaoUpdate, ServidorUpdate, AlunoUpdate, SolicitacaoUpdate, HistoricoUpdate
from .views import CampusDelete, CursoDelete, StatusDelete, TipoSolicitacaoDelete, ServidorDelete, AlunoDelete, SolicitacaoDelete, HistoricoDelete
from .views import CampusList

urlpatterns = [
    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),
    path("cadastrar/curso/", CursoCreate.as_view(), name="cadastrar-curso"),
    path("cadastrar/status/", StatusCreate.as_view(), name="cadastrar-status"),
    path("cadastrar/tipo-solicitacao/", TipoSolicitacaoCreate.as_view(), name="cadastrar-tipo-solicitacao"),
    path("cadastrar/servidor/", ServidorCreate.as_view(), name="cadastrar-servidor"),
    path("cadastrar/aluno/", AlunoCreate.as_view(), name="cadastrar-aluno"),
    path("cadastrar/solicitacao/", SolicitacaoCreate.as_view(), name="cadastrar-solicitacao"),
    path("cadastrar/historico/", HistoricoCreate.as_view(), name="cadastrar-historico"),

    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),
    path("editar/curso/<int:pk>/", CursoUpdate.as_view(), name="editar-curso"),
    path("editar/status/<int:pk>/", StatusUpdate.as_view(), name="editar-status"),
    path("editar/tipo-solicitacao/<int:pk>/", TipoSolicitacaoUpdate.as_view(), name="editar-tipo-solicitacao"),
    path("editar/servidor/<int:pk>/", ServidorUpdate.as_view(), name="editar-servidor"),
    path("editar/aluno/<int:pk>/", AlunoUpdate.as_view(), name="editar-aluno"),
    path("editar/solicitacao/<int:pk>/", SolicitacaoUpdate.as_view(), name="editar-solicitacao"),
    # path("editar/historico/<int:pk>/", HistoricoUpdate.as_view(), name="editar-historico"),

    path("excluir/campus/<int:pk>/", CampusDelete.as_view(), name="excluir-campus"),
    path("excluir/curso/<int:pk>/", CursoDelete.as_view(), name="excluir-curso"),
    path("excluir/status/<int:pk>/", StatusDelete.as_view(), name="excluir-status"),
    path("excluir/tipo-solicitacao/<int:pk>/", TipoSolicitacaoDelete.as_view(), name="excluir-tipo-solicitacao"),
    path("excluir/servidor/<int:pk>/", ServidorDelete.as_view(), name="excluir-servidor"),
    path("excluir/aluno/<int:pk>/", AlunoDelete.as_view(), name="excluir-aluno"),
    path("excluir/solicitacao/<int:pk>/", SolicitacaoDelete.as_view(), name="excluir-solicitacao"),
    path("excluir/historico/<int:pk>/", HistoricoDelete.as_view(), name="excluir-historico"),

    path("listar/campi/", CampusList.as_view(), name="listar-campus"),

]