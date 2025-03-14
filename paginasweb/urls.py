from django.urls import path
# Importar suas views
from .views import PaginaInicial

urlpatterns = [
    path("", PaginaInicial.as_view(), name="index" ),
]