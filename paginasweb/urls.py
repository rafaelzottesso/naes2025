from django.urls import path
# Importar suas views
from .views import PaginaInicial, SobreView

urlpatterns = [
    path("", PaginaInicial.as_view(), name="index" ),
    path("sobre/", SobreView.as_view(), name="sobre"),
]