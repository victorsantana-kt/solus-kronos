# Generated by Django 4.1.7 on 2023-11-29 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo_notas_fiscais', '0009_alter_notafiscal_boleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='boleto',
            field=models.FileField(blank=True, null=True, upload_to='boletos/'),
        ),
    ]
