from django.core.validators import MinValueValidator
from django.db import models
import datetime

# Create your models here.

class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Laboratorio'
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='nombre')
    laboratorio = models.OneToOneField('Laboratorio', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Director General'
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'

    def __str__(self):
        return self.nombre

anios_choices = []

for i in range(2015, (datetime.datetime.now().year+1)):
    anios_choices.append((i, i))

def anio_actual():
    return datetime.date.today().year

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='Producto')
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=anios_choices, default=anio_actual, verbose_name='F Fabricación')
    p_costo = models.DecimalField(null=False, max_digits=12, decimal_places=2, verbose_name='P Costo')
    p_venta = models.DecimalField(null=False, max_digits=12, decimal_places=2, verbose_name='P Venta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
    

    