from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=256)
    categoria = models.CharField(max_length=256)
    cantidad = models.CharField(max_length=2)
    tamaño = models.CharField(max_length=256)
    forma = models.CharField(max_length=32,null=True)
    precio = models.CharField(max_length=32)
    material = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.codigo_producto} ({self.categoria},{self.precio})"

class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=256)
    tipo_pedido = models.CharField(max_length=11)
    lugar = models.CharField(max_length=256)
    tipo_envio = models.CharField(max_length=256)
    direccion_pedido = models.CharField(max_length=256)
    telefono = models.CharField(max_length=20, blank=True)
    email_contacto = models.EmailField(blank=True)
    
    def __str__(self):
        return f"{self.razon_social} ({self.numero_ruc})"
