# Ejercicio Tienda de Libros:
# El usuario debe proporcionar:
#   - el nombre, el id, precio, envio pago/gratis

print('Proporcione lo siguiente: ')
titulo = input('Título del libro: ')
codigo = int(input('ID del libro: '))
precio = float(input('Ingrese el precio: '))
envio = input('envio gratis? ingrese (True/False): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    print('ERROR, solo ingrese True o False')
    envio = input('envio gratis? ingrese (True/False): ')

print(f'''
    Título: {titulo},
    Código: {codigo},
    Precio: ${precio},
    Envio grauito? {envio}
''')
