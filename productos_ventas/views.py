from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from productos_ventas.forms import ClienteFormulario,PedidoFormulario,ProductoFormulario
from productos_ventas.models import Cliente,Pedido,Producto
#Creacion de vistas con funciones
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
        "pedido": Pedido.objects.all(), 
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

@login_required
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
            cliente = Cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono, direccion=direccion, dni=dni, fecha_nacimiento=fecha_nacimiento, creador=request.user)
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

@login_required
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
            producto = Producto(codigo_producto=codigo_producto, categoria=categoria, cantidad=cantidad, tamaño=tamaño, forma=forma, precio=precio, material=material,creador=request.user)
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

@login_required
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
            producto = Pedido(codigo_pedido=codigo_pedido, tipo_pedido=tipo_pedido, lugar=lugar, tipo_envio=tipo_envio, direccion_pedido=direccion_pedido, telefono=telefono, email_contacto=email_contacto,creador=request.user)
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
    

@login_required
def eliminar_cliente(request, id):
    # obtienes el cliente de la base de datos
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        cliente.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_cliente')
        return redirect(url_exitosa)
    
@login_required
def eliminar_producto(request, id):
    # obtienes el producto de la base de datos
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        producto.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_producto')
        return redirect(url_exitosa)
    
@login_required
def eliminar_pedido(request, id):
    # obtienes el curso de la base de datos
    pedido = Pedido.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        pedido.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_pedido')
        return redirect(url_exitosa)

@login_required
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            # modificamos el objeto en memoria RAM
            cliente.nombre = data["nombre"]
            cliente.apellido = data["apellido"]
            cliente.email = data["email"]
            cliente.telefono = data["telefono"]
            cliente.direccion = data["direccion"]
            cliente.dni = data["dni"]
            cliente.fecha_nacimiento = data["fecha_nacimiento"]
            # Los cambios se guardan en la Base de datos
            cliente.save()

            url_exitosa = reverse('lista_cliente')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'email':cliente.email,
            'telefono':cliente.telefono,
            'direccion':cliente.direccion,
            'dni':cliente.dni,
            'fecha_nacimiento':cliente.fecha_nacimiento,
        }
        formulario = ClienteFormulario(initial=inicial)
    return render(
        request=request,
        template_name='productos_ventas/formulario_cliente.html',
        context={'formulario': formulario},
    )

@login_required
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            # modificamos el objeto en memoria RAM
            producto.codigo_producto = data["codigo_producto"]
            producto.categoria = data["categoria"]
            producto.cantidad = data["cantidad"]
            producto.tamaño = data["tamaño"]
            producto.forma = data["forma"]
            producto.precio = data["precio"]
            producto.material = data["material"]
            # Los cambios se guardan en la Base de datos
            producto.save()

            url_exitosa = reverse('lista_producto')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'codigo_producto': producto.nombre,
            'categoria': producto.apellido,
            'cantidad':producto.email,
            'tamaño':producto.telefono,
            'forma':producto.direccion,
            'precio':producto.dni,
            'material':producto.fecha_nacimiento,
        }
        formulario = ProductoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='productos_ventas/formulario_producto.html',
        context={'formulario': formulario},
    )

@login_required
def editar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        formulario = PedidoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            # modificamos el objeto en memoria RAM
            pedido.codigo_pedido = data["codigo_pedido"]
            pedido.tipo_pedido = data["tipo_pedido"]
            pedido.lugar = data["lugar"]
            pedido.tipo_envio = data["tipo_envio"]
            pedido.direccion_pedido = data["direccion_pedido"]
            pedido.telefono = data["telefono"]
            pedido.email_contacto = data["email_contacto"]
            # Los cambios se guardan en la Base de datos
            pedido.save()

            url_exitosa = reverse('lista_pedido')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'codigo_producto': pedido.codigo_pedido,
            'tipo_pedido': pedido.tipo_pedido,
            'lugar':pedido.lugar,
            'tipo_envio':pedido.tipo_envio,
            'direccion_pedido':pedido.direccion_pedido,
            'telefono':pedido.telefono,
            'email_contacto':pedido.email_contacto,
        }
        formulario = PedidoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='productos_ventas/formulario_pedido.html',
        context={'formulario': formulario},
    )