class Producto:
    contador_preductos = 0

    def __init__(self, nombre: str, precio: float) -> None:
        Producto.contador_preductos += 1
        self.id_producto = Producto.contador_preductos
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f'''
            Id Producto {self.id_producto}:
            {self.nombre}______________${self.precio}
        '''

# pruebas solo para esta clase

if __name__ == '__main__':
    producto_1 = Producto('Remera', 1330.00)
    print(producto_1)
    producto_2 = Producto('Campera', 7500.00)
    print(producto_2)
