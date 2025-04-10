from django.db import models

# Create your models here.


class Status(models.Model):
    nome = models.CharField(max_length=50)

    # Método "toString" para imprimir objetos
    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = "Status"
        ordering = ["nome"]



class TipoSolicitacao(models.Model):

    descricao = models.CharField(max_length=100, verbose_name="descrição")
    prazo_externo = models.CharField(max_length=200)
    prazo_externo_dias = models.PositiveSmallIntegerField(
        help_text="Informe quantos dias úteis é o prazo de solicitação",
        blank=True, default=0)
    prazo_interno = models.CharField(max_length=200)
    prazo_interno_dias = models.PositiveSmallIntegerField(
        help_text="Informe quantos dias úteis para atendimento",
        blank=True, default=0)

    def __str__(self):
        if(self.prazo_externo_dias > 0):
            return f"{self.descricao} - Prazo: {self.prazo_externo_dias} dia(s)"
        else:
            return f"{self.descricao}"

    class Meta:
        verbose_name = "Tipo de Solicitação"
        verbose_name_plural = "Tipos de Solicitação"
        ordering = ["descricao"]



class Solicitacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="descrição")
    turma = models.CharField(max_length=50)

    tipo_solicitacao = models.ForeignKey(
        TipoSolicitacao, on_delete=models.PROTECT, 
        verbose_name="tipo de solicitação")

    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo_solicitacao} - {self.cadastrado_em}"

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"
        ordering = ["-cadastrado_em"]
