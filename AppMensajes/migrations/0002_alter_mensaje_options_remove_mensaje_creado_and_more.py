# Generated by Django 4.1 on 2022-09-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensaje',
            options={},
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='creado',
        ),
        migrations.DeleteModel(
            name='Hilo',
        ),
    ]
