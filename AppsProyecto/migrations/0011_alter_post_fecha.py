# Generated by Django 4.1 on 2022-09-28 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppsProyecto', '0010_delete_deportes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date(2022, 9, 28), null=True),
        ),
    ]