# Generated by Django 4.1.7 on 2023-12-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app477', '0007_alter_bd477_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd477',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
