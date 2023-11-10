from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q

from interesados_ventas.forms import PersonaNaturalFormulario,PersonaJuridicaFormulario,ProductoFormulario,ProductoEntregadoFormulario,ServiciosFormulario
from interesados_ventas.models import PersonaNatural,PersonaJuridica,Producto,Servicios,ProductoEntregado

# Create your views here.
def listar_persona_natural(request):
    contexto = {
        "person_natural": PersonaNatural.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="interesados_ventas/lista_persona_natural.html",
        context=contexto,
    )
    return http_response

def listar_persona_juridica(request):
    contexto = {
        "person_juridica": PersonaJuridica.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="interesados_ventas/lista_persona_juridica.html",
        context=contexto,
    )
    return http_response

def listar_producto(request):
    contexto = {
        "producto": Producto.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="interesados_ventas/lista_producto.html",
        context=contexto,
    )
    return http_response

def listar_servicios(request):
    contexto = {
        "servicios": Servicios.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="interesados_ventas/lista_servicios.html",
        context=contexto,
    )
    return http_response

def listar_producto_entregado(request):
    contexto = {
        "producto_entre": ProductoEntregado.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="interesados_ventas/lista_entregado.html",
        context=contexto,
    )
    return http_response

def crear_persona_natural(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = PersonaNaturalFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            telefono = data["telefono"]
            direccion = data["direccion"]
            dni = data["dni"]
            fecha_nacimiento = data["fecha_nacimiento"]

            # creo una persona natural en memoria RAM
            personanatural = PersonaNatural(nombre=nombre, apellido=apellido, email=email, telefono=telefono, direccion=direccion, dni=dni, fecha_nacimiento=fecha_nacimiento)
            # Lo guardan en la Base de datos
            personanatural.save()
            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_persona_natural')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = PersonaNaturalFormulario()
    http_response = render(
        request=request,
        template_name='interesados_ventas/formulario_pn.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_persona_juridica(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = PersonaJuridicaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            razon_social = data["razon_social"]
            numero_ruc = data["numero_ruc"]
            tipo_contribuyente = data["tipo_contribuyente"]
            tipo_actividad = data["tipo_actividad"]
            nombre_comercial = data["nombre_comercial"]
            direccion_fiscal = data["direccion_fiscal"]
            telefono = data["telefono"]
            email = data["email"]

            # creo una persona natural en memoria RAM
            personajuridica = PersonaJuridica(razon_social=razon_social, numero_ruc=numero_ruc, tipo_contribuyente=tipo_contribuyente, 
            tipo_actividad=tipo_actividad, nombre_comercial=nombre_comercial, direccion_fiscal=direccion_fiscal, email=email, telefono=telefono)
            # Lo guardan en la Base de datos
            personajuridica.save()
            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_pj')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = PersonaJuridicaFormulario()
    http_response = render(
        request=request,
        template_name='interesados_ventas/formulario_pj.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_producto(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            codigo_producto = data["codigo_producto"]
            categoria = data["categoria"]
            cantidad = data["cantidad"]
            tamaño = data["tamaño"]
            forma = data["forma"]
            precio = data["precio"]
            material = data["material"]

            # creo una persona natural en memoria RAM
            producto = Producto(codigo_producto=codigo_producto, categoria=categoria, cantidad=cantidad, tamaño=tamaño, forma=forma, precio=precio, material=material)
            # Lo guardan en la Base de datos
            producto.save()
            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_producto')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = ProductoFormulario()
    http_response = render(
        request=request,
        template_name='interesados_ventas/formulario_producto.html',
        context={'formulario': formulario}
    )
    return http_response


def crear_servicios(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ServiciosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            tipo_servicio = data["tipo_servicio"]
            precio = data["precio"]
            duracion = data["duracion"]
            lugar_servicio = data["lugar_servicio"]

            # creo una persona natural en memoria RAM
            servicios = Servicios(tipo_servicio=tipo_servicio, precio=precio, duracion=duracion, lugar_servicio=lugar_servicio)
            # Lo guardan en la Base de datos
            servicios.save()
            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_servicios')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = ServiciosFormulario()
    http_response = render(
        request=request,
        template_name='interesados_ventas/formulario_servicios.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_producto_entregado(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ProductoEntregadoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            codigo_producto_entregado = data["codigo_producto_entregado"]
            fecha_entrega = data["fecha_entrega"]
            estado_de_entrega = data["estado_de_entrega"]

            # creo una persona natural en memoria RAM
            servicios = ProductoEntregado(codigo_producto_entregado=codigo_producto_entregado, fecha_entrega=fecha_entrega, estado_de_entrega=estado_de_entrega)
            # Lo guardan en la Base de datos
            servicios.save()
            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_entregados')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = ProductoEntregadoFormulario()
    http_response = render(
        request=request,
        template_name='interesados_ventas/formulario_entregados.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_persona_natural(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        personanatural = PersonaNatural.objects.filter(
            Q(nombre__icontains=busqueda) | Q(apellido__contains=busqueda)
        )

        contexto = {
            "person_natural": personanatural,
        }
        http_response = render(
            request=request,
            template_name='interesados_ventas/lista_persona_natural.html',
            context=contexto,
        )
        return http_response

def buscar_persona_juridica(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        personajuridica = PersonaJuridica.objects.filter(
            Q(razon_social__icontains=busqueda) | Q(numero_ruc__contains=busqueda)
        )

        contexto = {
            "person_juridica": personajuridica,
        }
        http_response = render(
            request=request,
            template_name='interesados_ventas/lista_persona_juridica.html',
            context=contexto,
        )
        return http_response
    
def buscar_producto(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        producto = Producto.objects.filter(
            Q(codigo_producto__icontains=busqueda) | Q(categoria__contains=busqueda)
        )

        contexto = {
            "producto": producto,
        }
        http_response = render(
            request=request,
            template_name='interesados_ventas/lista_producto.html',
            context=contexto,
        )
        return http_response
    
def buscar_servicios(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        servicios = Servicios.objects.filter(
            Q(tipo_servicio__icontains=busqueda) | Q(lugar_servicio__contains=busqueda)
        )

        contexto = {
            "servicios": servicios,
        }
        http_response = render(
            request=request,
            template_name='interesados_ventas/lista_servicios.html',
            context=contexto,
        )
        return http_response
    
def buscar_producto_entregado(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        productoentre = ProductoEntregado.objects.filter(
            Q(codigo_producto_entregado__icontains=busqueda) | Q(fecha_entrega__contains=busqueda)
        )

        contexto = {
            "productoentre": productoentre,
        }
        http_response = render(
            request=request,
            template_name='interesados_ventas/lista_entregado.html',
            context=contexto,
        )
        return http_response