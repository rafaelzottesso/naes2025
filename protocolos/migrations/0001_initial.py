# Generated by Django 4.2.5 on 2025-04-10 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("nome", models.CharField(max_length=50)),
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
                    models.CharField(max_length=100, verbose_name="descrição"),
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
                (
                    "descricao",
                    models.CharField(max_length=100, verbose_name="descrição"),
                ),
                ("turma", models.CharField(max_length=50)),
                ("cadastrado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="protocolos.status",
                    ),
                ),
                (
                    "tipo_solicitacao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="protocolos.tiposolicitacao",
                        verbose_name="tipo de solicitação",
                    ),
                ),
            ],
            options={
                "verbose_name": "Solicitação",
                "verbose_name_plural": "Solicitações",
                "ordering": ["-cadastrado_em"],
            },
        ),
    ]
