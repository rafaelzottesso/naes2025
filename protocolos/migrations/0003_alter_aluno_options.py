# Generated by Django 4.2.5 on 2025-04-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocolos', '0002_alter_aluno_options_alter_servidor_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ['nome']},
        ),
    ]
