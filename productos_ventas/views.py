from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q

from productos_ventas.forms import ClienteFormulario,PedidoFormulario,ProductoFormulario
from productos_ventas.models import Cliente,Pedido,Producto

# Create your views here.
def listar_cliente(request):
    contexto = {
        "cliente": Cliente.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="productos_ventas/lista_cliente.html",
        context=contexto,
    )
    return http_response

def listar_pedido(request):
    contexto = {
        "person_juridica": Pedido.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="productos_ventas/lista_pedido.html",
        context=contexto,
    )
    return http_response

def listar_producto(request):
    contexto = {
        "producto": Producto.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name="productos_ventas/lista_producto.html",
        context=contexto,
    )
    return http_response

def crear_cliente(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            telefono = data["telefono"]
            direccion = data["direccion"]
            dni = data["dni"]
            fecha_nacimiento = data["fecha_nacimiento"]

            # creo un cliente en memoria RAM
            cliente = Cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono, direccion=direccion, dni=dni, fecha_nacimiento=fecha_nacimiento)
            # Lo guardan en la Base de datos
            cliente.save()
            # Redirecciono al usuario a la lista clientes
            url_exitosa = reverse('lista_cliente')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = ClienteFormulario()
    http_response = render(
        request=request,
        template_name='productos_ventas/formulario_cliente.html',
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

            # creo un producto en memoria RAM
            producto = Producto(codigo_producto=codigo_producto, categoria=categoria, cantidad=cantidad, tamaño=tamaño, forma=forma, precio=precio, material=material)
            # Lo guardan en la Base de datos
            producto.save()
            # Redirecciono al usuario a la lista productos
            url_exitosa = reverse('lista_producto')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = ProductoFormulario()
    http_response = render(
        request=request,
        template_name='productos_ventas/formulario_producto.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_pedido(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = PedidoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            codigo_pedido = data["codigo_pedido"]
            tipo_pedido = data["tipo_pedido"]
            lugar = data["lugar"]
            tipo_envio = data["tipo_envio"]
            direccion_pedido = data["direccion_pedido"]
            telefono = data["telefono"]
            email_contacto = data["email_contacto"]

            # creo un pedido en la memoria RAM
            producto = Pedido(codigo_pedido=codigo_pedido, tipo_pedido=tipo_pedido, lugar=lugar, tipo_envio=tipo_envio, direccion_pedido=direccion_pedido, telefono=telefono, email_contacto=email_contacto)
            # Lo guardan en la Base de datos
            producto.save()
            # Redirecciono al usuario a la lista de pedidos
            url_exitosa = reverse('lista_pedido')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = PedidoFormulario()
    http_response = render(
        request=request,
        template_name='productos_ventas/formulario_pedido.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cliente = Cliente.objects.filter(
            Q(nombre__icontains=busqueda) | Q(apellido__contains=busqueda)
        )

        contexto = {
            "cliente": cliente,
        }
        http_response = render(
            request=request,
            template_name='productos_ventas/lista_cliente.html',
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
            template_name='productos_ventas/lista_producto.html',
            context=contexto,
        )
        return http_response

def buscar_pedido(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        pedido = Pedido.objects.filter(
            Q(codigo_producto__icontains=busqueda) | Q(categoria__contains=busqueda)
        )

        contexto = {
            "pedido": pedido,
        }
        http_response = render(
            request=request,
            template_name='productos_ventas/lista_pedido.html',
            context=contexto,
        )
        return http_response
