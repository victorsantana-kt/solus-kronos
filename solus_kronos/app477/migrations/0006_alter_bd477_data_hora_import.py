# Generated by Django 4.1.7 on 2023-12-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app477', '0005_bd477_data_hora_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd477',
            name='data_hora_import',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
