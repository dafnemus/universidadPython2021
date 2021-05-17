# Ejercicio Mayor de edad:

# Pedirle al usuario que ingrese su edad.
# Determinar si el usuario es mayor de edad.

edad = int(input('Cuántos años tenes?: '))

edad_adulto = 18

if edad >= edad_adulto:
    print(f'Si tienes {edad}. Eres mayor de edad')
else:
    print(f'Si tienes {edad}. Eres menor de edad')
