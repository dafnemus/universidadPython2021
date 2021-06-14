from Producto import Producto
from Orden import Orden

producto_1 = Producto('Remera', 1330.00)
print(producto_1)

producto_2 = Producto('Campera', 7500.00)
lista_productos_1 = [producto_2, producto_1]

# orden simple con la lista definida y su total
orden_1 = Orden(lista_productos_1)
print(orden_1)
print(f'Total= ${orden_1.calcular_total_orden()}')

# orden a la que se la agrega un producto mas.
orden_2 = Orden(lista_productos_1)
print(orden_2)
producto_3 = Producto('Zapatos', 8599.99)
orden_2.agregar_producto(producto_3)
print(orden_2)
print(f'Total= ${orden_2.calcular_total_orden()}')
