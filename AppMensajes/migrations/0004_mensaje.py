# Generated by Django 4.1 on 2022-09-28 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppMensajes', '0003_modelbase_delete_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppMensajes.modelbase')),
                ('texto', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('AppMensajes.modelbase',),
        ),
    ]
