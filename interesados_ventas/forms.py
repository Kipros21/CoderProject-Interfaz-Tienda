from django import forms

class PersonaNaturalFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=256)
    apellido = forms.CharField(required=True,max_length=256)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True,max_length=20)
    direccion = forms.CharField(required=True,max_length=256)
    dni = forms.CharField(required=True,max_length=32)
    fecha_nacimiento = forms.DateField(required=True)

class PersonaJuridicaFormulario(forms.Form):

    razon_social = forms.CharField(required=True,max_length=256)
    numero_ruc = forms.CharField(required=True,max_length=11)
    tipo_contribuyente = forms.CharField(required=True,max_length=256)
    tipo_actividad = forms.CharField(required=True,max_length=256)
    nombre_comercial = forms.CharField(required=True,max_length=256)
    direccion_fiscal = forms.CharField(required=True,max_length=256)
    telefono = forms.CharField(required=True,max_length=20)
    email = forms.EmailField(required=True)


class ProductoFormulario(forms.Form):
    codigo_producto = forms.CharField(required=True, max_length=256)
    categoria = forms.CharField(required=True, max_length=256)
    cantidad = forms.CharField(required=True, max_length=2)
    tamaño = forms.CharField(required=True, max_length=256)
    forma = forms.CharField(required=True, max_length=32)
    precio = forms.CharField(required=True, max_length=32)
    material = forms.CharField(required=True, max_length=256)

class ServiciosFormulario(forms.Form):
    tipo_servicio = forms.CharField(required=True,max_length=256)
    precio = forms.CharField(required=True,max_length=32)
    duracion = forms.CharField(required=True,max_length=32)
    lugar_servicio = forms.CharField(required=True,max_length=256)

class ProductoEntregadoFormulario(forms.Form):
    codigo_producto_entregado = forms.CharField(required=True,max_length=256)
    fecha_entrega = forms.DateTimeField(required=True)
    estado_de_entrega = forms.BooleanField(required=True)