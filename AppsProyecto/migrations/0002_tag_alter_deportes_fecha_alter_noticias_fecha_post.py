# Generated by Django 4.1 on 2022-09-13 01:27

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppsProyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='deportes',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date(2022, 9, 12), null=True),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date(2022, 9, 12), null=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='post')),
                ('state', models.BooleanField(default=False, verbose_name='Active')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='AppsProyecto.tag')),
            ],
        ),
    ]