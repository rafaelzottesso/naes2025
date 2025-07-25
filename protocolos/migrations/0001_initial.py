# Generated by Django 4.2.20 on 2025-07-24 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Campus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=120)),
            ],
            options={
                "verbose_name_plural": "Campi",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                (
                    "campus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="protocolos.campus",
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("ordem", models.PositiveIntegerField(unique=True)),
                ("pode_editar", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Status",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="TipoSolicitacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "descricao",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="descrição"
                    ),
                ),
                ("prazo_externo", models.CharField(max_length=200)),
                (
                    "prazo_externo_dias",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        default=0,
                        help_text="Informe quantos dias úteis é o prazo de solicitação",
                    ),
                ),
                ("prazo_interno", models.CharField(max_length=200)),
                (
                    "prazo_interno_dias",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        default=0,
                        help_text="Informe quantos dias úteis para atendimento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tipo de Solicitação",
                "verbose_name_plural": "Tipos de Solicitação",
                "ordering": ["descricao"],
            },
        ),
        migrations.CreateModel(
            name="Solicitacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("turma", models.CharField(max_length=30)),
                ("justificativa", models.TextField()),
                (
                    "anexo",
                    models.FileField(
                        blank=True, null=True, upload_to="anexos_solicitacao/"
                    ),
                ),
                ("solicitado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="protocolos.curso",
                    ),
                ),
                (
                    "solicitado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tipo_solicitacao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="protocolos.tiposolicitacao",
                    ),
                ),
            ],
            options={
                "verbose_name": "Solicitação",
                "verbose_name_plural": "Solicitações",
                "ordering": ["-solicitado_em"],
            },
        ),
        migrations.CreateModel(
            name="Servidor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("siape", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=254)),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Servidores",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Historico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gerado_em", models.DateTimeField(auto_now_add=True)),
                (
                    "gerado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "solicitacao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="protocolos.solicitacao",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="protocolos.status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Histórico",
                "verbose_name_plural": "Históricos",
                "ordering": ["-gerado_em"],
            },
        ),
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("matricula", models.CharField(max_length=50, unique=True)),
                ("cpf", models.CharField(max_length=14, unique=True)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=20)),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
    ]
