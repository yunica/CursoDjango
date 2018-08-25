from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    isuso = models.BooleanField(default=True)
    registro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
        
class SubCategoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    isuso = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    registro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)   
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True,upload_to='productos/')
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    precio_oferta = models.DecimalField(max_digits=19, decimal_places=4, blank=True)
    registro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)   
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True,upload_to='proveedores/')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre






class Compra(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    precio_total = models.DecimalField(max_digits=19, decimal_places=4,blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True, default=0)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.PROTECT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

class CompraDetalle(models.Model):
    precio_total = models.DecimalField(max_digits=19, decimal_places=4,blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True, default=0)
    producto = models.ForeignKey(Producto,on_delete=models.PROTECT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def actualizarstock(self):
        if self.producto:
            oproducto = self.producto
            oproducto.cantidad = oproducto.cantidad + self.cantidad
            oproducto.save()

@transaction.atomic
@receiver(post_save, sender=CompraDetalle)
def agregarstock(sender, instance, created, **kwargs):
    if created:
        instance.actualizarstock()