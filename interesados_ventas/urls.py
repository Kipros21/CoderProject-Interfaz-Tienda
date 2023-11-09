from django.urls import path
from interesados_ventas.views import listar_estudiantes
# Estas son las URLS de la app interesados_ventas
urlpatterns = [
    path("estudiantes/",listar_estudiantes),
]