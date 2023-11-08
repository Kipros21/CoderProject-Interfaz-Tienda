from django.db import models

# Create your models here.
class PersonaNatural(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

class PersonaJuridica(models.Model):
    razon_social = models.CharField(max_length=256)
    numero_ruc = models.CharField(max_length=11)
    tipo_contribuyente = models.CharField(max_length=256)
    tipo_actividad = models.CharField(max_length=256)
    nombre_comercial = models.CharField(max_length=256)
    direccion_fiscal = models.CharField(max_length=256)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    
class Producto(models.Model):
    codigo_producto = models.CharField(max_length=256)
    categoria = models.CharField(max_length=256)
    cantidad = models.CharField(max_length=2)
    tamaño = models.CharField(max_length=256)
    forma = models.CharField(max_length=32,null=True)
    precio = models.CharField(max_length=32)
    material = models.CharField(max_length=256)

class Servicios(models.Model):
    tipo_servicio = models.CharField(max_length=256)
    precio = models.CharField(max_length=32)
    duracion = models.CharField(max_length=32)
    lugar_servicio = models.CharField(max_length=256)

class ProductoEntregado(models.Model):
    codigo_producto_entregado = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    estado_de_entrega = models.BooleanField(default=False)