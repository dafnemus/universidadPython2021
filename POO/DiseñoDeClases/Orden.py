from Producto import Producto


class Orden:

    contador_ordenes = 0

    def __init__(self, productos) -> None:
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.productos = list(productos)

    def agregar_producto(self, producto_nuevo):
        self.productos.append(producto_nuevo)

    def calcular_total_orden(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self) -> str:
        productos = ''
        for producto in self.productos:
            productos += producto.__str__() + '\n'
        return f'''
            Orden: {self.id_orden}
            {productos}
        '''


if __name__ == '__main__':
    producto_1 = Producto('Remera', 1330.00)
    producto_2 = Producto('Campera', 7500.00)
    lista_productos_1 = [producto_2, producto_1]
    orden_1 = Orden(lista_productos_1)
    print(orden_1)
