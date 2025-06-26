from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Campus(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Campi"


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} ({self.campus.nome})'
    
    class Meta:
        ordering = ["nome"]


class Status(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField(unique=True)
    pode_editar = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Status"
        ordering = ["nome"]


class TipoSolicitacao(models.Model):

    descricao = models.CharField(max_length=100, verbose_name="descrição", unique=True)
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


class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=14, unique=True) 
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]


class Servidor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    siape = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Servidores"


class Solicitacao(models.Model):
    solicitado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    turma = models.CharField(max_length=30)
    tipo_solicitacao = models.ForeignKey(TipoSolicitacao, on_delete=models.PROTECT)
    justificativa = models.TextField()
    anexo = models.FileField(upload_to='anexos_solicitacao/', blank=True, null=True)
    solicitado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo_solicitacao} - {self.solicitado_em}"

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"
        ordering = ["-solicitado_em"]


class Historico(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    gerado_em = models.DateTimeField(auto_now_add=True)
    gerado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.solicitacao} - {self.status.nome} em {self.gerado_em:%d/%m/%Y %H:%M}'
    
    class Meta:
        verbose_name = "Histórico"
        verbose_name_plural = "Históricos"
        ordering = ["-gerado_em"]