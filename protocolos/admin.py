from django.contrib import admin
from .models import Solicitacao, Status, TipoSolicitacao, Historico
from .models import Aluno, Servidor, Campus, Curso

# Register your models here.
admin.site.register(Solicitacao)
admin.site.register(Status)
admin.site.register(TipoSolicitacao)
admin.site.register(Historico)
admin.site.register(Aluno)
admin.site.register(Servidor)
admin.site.register(Campus)
admin.site.register(Curso)

