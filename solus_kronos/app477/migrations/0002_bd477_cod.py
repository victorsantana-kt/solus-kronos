# Generated by Django 4.2.7 on 2023-12-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app477', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd477',
            name='cod',
            field=models.TextField(blank=True, null=True),
        ),
    ]
