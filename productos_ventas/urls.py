from django.urls import path
from productos_ventas.views import (listar_cliente,listar_producto,listar_pedido,
                                    crear_cliente,crear_producto,crear_pedido,
                                    buscar_cliente,buscar_producto,buscar_pedido)
# Estas son las URLS de la app productos_ventas
urlpatterns = [
    path("cliente/",listar_cliente, name="lista_cliente"),
    path("producto/",listar_producto, name="lista_producto"),
    path("pedido/",listar_pedido, name="lista_pedido"),

    path("crear-cliente/",crear_cliente,name="crear_cliente"),
    path("crear-producto/",crear_producto,name="crear_producto"),
    path("crear-pedido/",crear_pedido,name="crear_pedido"),

    path("buscar-cliente",buscar_cliente,name="buscar_pn"),
    path("buscar-producto",buscar_producto,name="buscar_producto"),
    path("buscar-pedido",buscar_pedido,name="buscar_pedido"),
]