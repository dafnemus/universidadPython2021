class ManejoArchivos:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    # apertura de archivos
    def __enter__(self):
        print('Archivo recibido'.center(30, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    # cierre de archivos, se requieren tres atributos para el metodo exit.
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Archivo Cerado'.center(30, '-'))
        if self.nombre:
            self.nombre.close()

