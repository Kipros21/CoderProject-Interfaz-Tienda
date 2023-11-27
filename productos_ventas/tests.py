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

class ProductoTests(TestCase):
    """En esta clase van todas las pruebas del modelo Producto."""

    def test_creacion_producto(self):
        # caso uso esperado
        producto = Producto(codigo_producto="SKU1025", categoria="Saborizante", cantidad=10, tamaño="Grande", forma="Redonda", precio=100, material="Especias")
        producto.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Producto.objects.count(), 1)
        self.assertEqual(producto.codigo_producto, "SKU1025")
        self.assertEqual(producto.categoria, "Saborizante")
        self.assertEqual(producto.cantidad, 10)
        self.assertEqual(producto.tamaño, "Grande")
        self.assertEqual(producto.forma, "Redonda")
        self.assertEqual(producto.precio, 100)
        self.assertEqual(producto.material, "Especias")


    def test_cliente_str(self):
        producto = Producto(codigo_producto="SKU1530", categoria="Calzado", precio=150)
        producto.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(producto.__str__(), "SKU1530 (Calzado,150)")

class PedidoTests(TestCase):
    """En esta clase van todas las pruebas del modelo Producto."""

    def test_creacion_pedido(self):
        # caso uso esperado
        pedido = Pedido(codigo_pedido="ENT4785", tipo_pedido="Urgente", lugar="Puerto Bermudez", tipo_envio="Aereo", direccion_pedido="Avenida del Sol", telefono=987456123, email_contacto="pepito31@hotmail.com")
        pedido.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(pedido.codigo_pedido, "ENT4785")
        self.assertEqual(pedido.tipo_pedido, "Urgente")
        self.assertEqual(pedido.lugar, "Puerto Bermudez")
        self.assertEqual(pedido.tipo_envio, "Aereo")
        self.assertEqual(pedido.direccion_pedido, "Avenida del Sol")
        self.assertEqual(pedido.telefono, 987456123)
        self.assertEqual(pedido.email_contacto, "pepito31@hotmail.com")


    def test_cliente_str(self):
        pedido = Pedido(codigo_pedido="ENT5687", direccion_pedido="Calle del Mar", email_contacto="techito4567@hotmail.com")
        pedido.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(pedido.__str__(), "ENT5687 (Calle del Mar,techito4567@hotmail.com)")