# Cadenas(String)

mi_grupo_favorito = 'BTS'
print(mi_grupo_favorito)

# Concatenación 

print('Mi grupo favorito es: ' + mi_grupo_favorito)

comentario = 'hace historia'
print(mi_grupo_favorito + ' ' + comentario)

mi_grupo_favorito += ' la mejor banda de Kpop'

print(mi_grupo_favorito)

# concatenación vs suma:
numero_1 = '2'
numero_2 = '4'

print('Concatenación: ', numero_1 + numero_2)

print('Suma:', int(numero_1) + int(numero_2))

# Funcion INPUT para procesar la entrada del usuario.
resultado = input('Escribe un mensaje: ')
print(f'mensaje: {resultado}')

# conversion de input a int.
num_1 = int(input('Escriba un número: '))
num_2 = int(input('Escriba un número: '))

print(f'{num_1} + {num_2} = {num_1 + num_2}')
