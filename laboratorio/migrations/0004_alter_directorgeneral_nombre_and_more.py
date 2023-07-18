# Generated by Django 4.2.2 on 2023-07-18 03:47

from django.db import migrations, models
import laboratorio.models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_alter_directorgeneral_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directorgeneral',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=laboratorio.models.anio_actual, verbose_name='F Fabricación'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='p_costo',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='P Costo'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='p_venta',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='P Venta'),
        ),
    ]
