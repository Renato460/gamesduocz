from django.contrib import admin

# Register your models here.
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    #Agregar restricciones del administrador
    #Que cosas el usuario no puede editar
    readonly_fields = ('created','update')

admin.site.register(Producto,ProductoAdmin)