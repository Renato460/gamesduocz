from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Producto(models.Model):
    """Modelo de Producto"""
    titulo = models.CharField(max_length=50, verbose_name="Titulo del Producto")
    descripcion = RichTextField(verbose_name="Detalle del Producto")
    imagen = models.ImageField(upload_to='productos', verbose_name="Imagen del Producto")
    precio = models.IntegerField(verbose_name="Precio del producto")
    estaEnOferta = models.BooleanField(verbose_name="Esta en oferta", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.titulo
    