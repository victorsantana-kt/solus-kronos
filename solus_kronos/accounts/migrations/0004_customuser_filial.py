# Generated by Django 4.2.7 on 2023-12-06 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filiais', '0003_filial_cliente'),
        ('accounts', '0003_alter_customuser_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='filiais.filial'),
        ),
    ]
