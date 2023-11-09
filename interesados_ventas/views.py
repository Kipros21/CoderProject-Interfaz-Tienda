from django.shortcuts import render
from interesados_ventas.models import PersonaNatural

# Create your views here.
def listar_estudiantes(request):
    contexto = {
        "profesor": "Pedro",
        "estudiantes": PersonaNatural.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="interesados_ventas/lista_estudiantes.html",
        context=contexto,
    )
    return http_response