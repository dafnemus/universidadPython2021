archivo = open('prueba.txt', 'r', encoding='utf8')
# crear un archivo 2 desde este archivo
archivo_2 = open('copia_pueba.txt', 'a')


try:
    # leer toda la info del archivo
    # print(archivo.read())
    # leer algunos caracteres
    print(archivo.read(5))
    # iterar un archivo
    for linea in archivo:
        print(linea)
    # leer las lineas de un archivo
    print(archivo.readline())
    # acceder a una linea especifica
    print(archivo.readlines()[-1])
    # con a = anexar
    archivo_2.write(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo_2.close()
    print('Archivo cerrado')
