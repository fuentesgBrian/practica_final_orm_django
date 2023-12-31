# Generated by Django 4.2.2 on 2023-07-15 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_alter_directorgeneral_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directorgeneral',
            options={'verbose_name': 'Director General', 'verbose_name_plural': 'Directores Generales'},
        ),
        migrations.AlterModelOptions(
            name='laboratorio',
            options={'verbose_name': 'Laboratorio', 'verbose_name_plural': 'Laboratorios'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelTable(
            name='laboratorio',
            table='Laboratorio',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='Producto',
        ),
    ]
