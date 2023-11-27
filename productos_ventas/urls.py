from django.urls import path
from productos_ventas.views import (listar_cliente,listar_producto,listar_pedido,
                                    crear_cliente,crear_producto,crear_pedido,
                                    buscar_cliente,buscar_producto,buscar_pedido,
                                    eliminar_cliente,eliminar_producto,eliminar_pedido,
                                    editar_cliente,editar_producto,editar_pedido)
# Estas son las URLS de la app productos_ventas
urlpatterns = [
    path("cliente/",listar_cliente, name="lista_cliente"),
    path("producto/",listar_producto, name="lista_producto"),
    path("pedido/",listar_pedido, name="lista_pedido"),

    path("crear-cliente/",crear_cliente,name="crear_cliente"),
    path("crear-producto/",crear_producto,name="crear_producto"),
    path("crear-pedido/",crear_pedido,name="crear_pedido"),

    path("buscar-cliente/",buscar_cliente,name="buscar_cliente"),
    path("buscar-producto/",buscar_producto,name="buscar_producto"),
    path("buscar-pedido/",buscar_pedido,name="buscar_pedido"),

    path("eliminar-cliente/<int:id>/", eliminar_cliente, name="eliminar_cliente"),
    path("eliminar-producto/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("eliminar-pedido/<int:id>/", eliminar_pedido, name="eliminar_pedido"),

    path("editar-cliente/<int:id>/", editar_cliente, name="editar_cliente"),
    path("editar-producto/<int:id>/", editar_producto, name="editar_producto"),
    path("editar-pedido/<int:id>/", editar_pedido, name="editar_pedido"),

]