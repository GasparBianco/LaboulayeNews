# Generated by Django 4.2.4 on 2023-10-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLaboulayeNews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='sinopsis',
            field=models.TextField(default='Breve descripcion de la noticia... Breve descripcion de la noticia.'),
            preserve_default=False,
        ),
    ]