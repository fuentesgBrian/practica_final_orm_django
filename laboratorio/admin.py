from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    fields = ['id', 'nombre']
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    ordering = ('id',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    fields = ['id', 'nombre', 'laboratorio']
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    fields = ['id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre', 'laboratorio')
    list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
