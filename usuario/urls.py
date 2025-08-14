from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import CadastroUsuarioView

urlpatterns = [
    
    path("login/", LoginView.as_view(
        template_name = "protocolos/form.html",
        extra_context={"titulo": "Autenticação"}), name="login"),
    
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("alterar-senha/", PasswordChangeView.as_view(
        template_name="protocolos/form.html",
        extra_context={"titulo": "Alterar minha senha"}), name="alterar-senha"),

    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

]


