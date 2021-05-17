# Operadores Lógicos:

# a AND b: devuelve TRUE si ambos son verdaderos
a = True
b = True
resultado = a and b
print(f'si a:{a} y b:{b}, entonces {resultado}')

a = True
b = False
resultado = a and b
print(f'si a:{a} y b:{b}, entonces {resultado}')

a = False
b = False
resultado = a and b
print(f'si a:{a} y b:{b}, entonces {resultado}')

# a OR b: devuelve TRUE si alguno es verdadero
a = True
b = True
resultado = a or b
print(f'si a:{a} o b:{b}, entonces {resultado}')

a = True
b = False
resultado = a or b
print(f'si a:{a} o b:{b}, entonces {resultado}')

a = False
b = False
resultado = a or b
print(f'si a:{a} o b:{b}, entonces {resultado}')

# (unario) NOT b: devuelve TRUE si alguno es FALSE
a = True
resultado = not a
print(f'si no a:{a}, entonces {resultado}')

a = False
resultado = not a
print(f'si no a:{a}, entonces {resultado}')
