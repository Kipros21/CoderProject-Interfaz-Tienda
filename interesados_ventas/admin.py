from django.contrib import admin
from interesados_ventas.models import PersonaJuridica,PersonaNatural,Producto,Servicios,ProductoEntregado
# Register your models here.
admin.site.register(PersonaJuridica)
admin.site.register(PersonaNatural)
admin.site.register(Producto)
admin.site.register(Servicios)
admin.site.register(ProductoEntregado)