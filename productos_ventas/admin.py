from django.contrib import admin
from productos_ventas.models import Cliente,Pedido,Producto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
