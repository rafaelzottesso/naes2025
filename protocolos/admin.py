from django.contrib import admin
from .models import Solicitacao, Status, TipoSolicitacao

# Register your models here.
admin.site.register(Solicitacao)
admin.site.register(Status)
admin.site.register(TipoSolicitacao)
