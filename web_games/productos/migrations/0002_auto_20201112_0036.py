# Generated by Django 3.1.3 on 2020-11-12 00:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Detalle del Producto'),
        ),
    ]