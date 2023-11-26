from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=256)
    apellido = forms.CharField(required=True,max_length=256)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True,max_length=20)
    direccion = forms.CharField(required=True,max_length=256)
    dni = forms.CharField(required=True,max_length=32)
    fecha_nacimiento = forms.DateField(required=True)

class ProductoFormulario(forms.Form):
    codigo_producto = forms.CharField(required=True, max_length=256)
    categoria = forms.CharField(required=True, max_length=256)
    cantidad = forms.CharField(required=True, max_length=2)
    tamaño = forms.CharField(required=True, max_length=256)
    forma = forms.CharField(required=True, max_length=32)
    precio = forms.CharField(required=True, max_length=32)
    material = forms.CharField(required=True, max_length=256)

class PedidoFormulario(forms.Form):
    codigo_pedido = forms.CharField(required=True, max_length=256)
    tipo_pedido = forms.CharField(required=True, max_length=256)
    lugar = forms.CharField(required=True, max_length=2)
    tipo_envio = forms.CharField(required=True, max_length=256)
    direccion_pedido = forms.CharField(required=True, max_length=32)
    telefono = forms.CharField(required=True, max_length=32)
    email_contacto = forms.CharField(required=True, max_length=256)
