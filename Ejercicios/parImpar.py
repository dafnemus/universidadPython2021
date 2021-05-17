# Ejercicio Par o Impar
# El usuario debe ingresar un número y se debe determinar si es PAR o IMPAR.

numero = int(input('Ingrese un Número entero: '))

if numero % 2 == 0:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')
