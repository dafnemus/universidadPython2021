import os

class Catalogo:
    ruta_archivo = 'catalogo-peliculas.txt'
    def __init__(self) -> None:
       self.archivo = open(Catalogo.ruta_archivo, 'a', encoding='utf8')

    def agregar_pelicula(self, pelicula):
        self.archivo.write(f'{pelicula.titulo} \n')

    def listar_peliculas(self):
        self.archivo = open(Catalogo.ruta_archivo, 'r')
        print(self.archivo.read())

    def eliminar_catalogo(self):
        os.remove(self.archivo)
        print('Archivo eliminado')
