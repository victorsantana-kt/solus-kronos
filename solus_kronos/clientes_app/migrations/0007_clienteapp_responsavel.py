# Generated by Django 4.2.7 on 2023-12-31 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes_app', '0006_remove_clienteapp_cliente_kronos'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteapp',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clientes_responsaveis', to=settings.AUTH_USER_MODEL),
        ),
    ]