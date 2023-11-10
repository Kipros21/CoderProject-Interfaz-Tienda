from django.urls import path
from interesados_ventas.views import (listar_persona_natural,listar_persona_juridica,listar_producto,listar_servicios,
                                      listar_producto_entregado,crear_persona_natural,crear_persona_juridica,crear_producto,
                                      crear_servicios,crear_producto_entregado,buscar_persona_natural,buscar_persona_juridica,buscar_producto,
                                      buscar_servicios,buscar_producto_entregado)
# Estas son las URLS de la app interesados_ventas
urlpatterns = [
    path("natural/",listar_persona_natural, name="lista_persona_natural"),
    path("juridica/",listar_persona_juridica, name="lista_persona_juridica"),
    path("producto/",listar_producto, name="lista_producto"),
    path("servicios/",listar_servicios, name="lista_servicios"),
    path("entregado/",listar_producto_entregado, name="lista_entregado"),
    path("crear-pn/",crear_persona_natural,name="crear_pn"),
    path("crear-pj/",crear_persona_juridica,name="crear_pj"),
    path("crear-producto/",crear_producto,name="crear_producto"),
    path("crear-servicios/",crear_servicios,name="crear_servicios"),
    path("crear-entregados",crear_producto_entregado,name="crear_entregados"),
    path("buscar-pn",buscar_persona_natural,name="buscar_pn"),
    path("buscar-pj",buscar_persona_juridica,name="buscar_pj"),
    path("buscar-producto",buscar_producto,name="buscar_producto"),
    path("buscar-servicios",buscar_servicios,name="buscar_servicios"),
    path("buscar-entregados",buscar_producto_entregado,name="buscar_entregados"),
]