# Generated by Django 5.0.3 on 2024-04-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticia_autora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(choices=[('Esporte', 'Esporte'), ('Cultura', 'Cultura'), ('Economia', 'Economia'), ('Política', 'Politica'), ('Tecnologia', 'Tecnologia')], max_length=50),
        ),
    ]
