# Generated by Django 5.0.3 on 2024-04-08 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_alter_noticia_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='sub_titulo',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='autora',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
