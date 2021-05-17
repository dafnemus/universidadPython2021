# Ejercicio Valor Dentro del Rango:
# Solicite un valor al usuario y determine si esta dentro del rango.

valor = int(input('Ingrese un numero: '))

if valor > 0 and valor <= 5:
    print(f'El valor {valor} está dentro del rango(1 al 5)')
else:
    print(f'El valor {valor} está fuera del rango(1 al 5)')
