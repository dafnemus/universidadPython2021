# Manejo 1 de archivos desde python
# w = write
# encodig = tipografía permitida
# close() = cierre de un archivo
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Este es un archivo de prueba\n')
    archivo.write('Esto es Python\n')
    archivo.write('Adiós!!!!!')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Archivo cerrado')
