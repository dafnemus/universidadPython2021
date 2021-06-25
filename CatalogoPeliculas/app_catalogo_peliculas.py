from Servicio.Catalogo import Catalogo
from Dominio.Pelicula import Pelicula

print('Catalogo de peliculas')
opcion = None
catalogo = Catalogo()
while opcion != 4:
    try:
        print('''
        Opciones:
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar Catalogo
        4. Salir 
        ''')
        opcion = int(input('Proporcione una opcion (1-4): '))
    except Exception as e:
        print(e)

    if opcion == 1:
        titulo_pelicula = input('Proporcione una pelicula: ')
        pelicula = Pelicula(titulo_pelicula)
        catalogo.agregar_pelicula(pelicula)
    if opcion == 2:
        catalogo.listar_peliculas()
    if opcion == 3:
        catalogo.eliminar_catalogo()
else:
    print('Gracias por usar nuesytro catalogo')
