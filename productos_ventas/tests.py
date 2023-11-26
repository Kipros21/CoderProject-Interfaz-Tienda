from django.test import TestCase

from productos_ventas.models import Cliente,Producto,Pedido


class ClienteTests(TestCase):
    """En esta clase van todas las pruebas del modelo Cliente."""

    def test_creacion_cliente(self):
        # caso uso esperado
        cliente = Cliente(nombre="Cristhian", apellido="Huanqui", email="kipros21@gmail.com", telefono=992857421, direccion="Lima", dni=71453258, fecha_nacimiento="1994-09-21")
        cliente.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(cliente.nombre, "Cristhian")
        self.assertEqual(cliente.apellido, "Huanqui")
        self.assertEqual(cliente.email, "kipros21@gmail.com")
        self.assertEqual(cliente.telefono, 992857421)
        self.assertEqual(cliente.direccion, "Lima")
        self.assertEqual(cliente.dni, 71453258)
        self.assertEqual(cliente.fecha_nacimiento, "1994-09-21")


    def test_cliente_str(self):
        cliente = Cliente(nombre="Jimmy", apellido="Auris")
        cliente.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(cliente.__str__(), "Jimmy, Auris")
