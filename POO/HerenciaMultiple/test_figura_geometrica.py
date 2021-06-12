from POO.HerenciaMultiple.Rectangulo import Rectangulo
from POO.HerenciaMultiple.Cuadrado import Cuadrado

# Clase abstracta:
# figura = FiguraGeometrica()

print('Creacion Cuadrados'.center(15, '-'))
cuadrado_1 = Cuadrado(10, 'verde')
print(cuadrado_1)
print(f'El area del cuadrado 1 es: {cuadrado_1.calcular_area()}')
print()

# si se ingresa un numero menor a 0 o un num > 10
# e valor por defecto es 0
cuadrado_2 = Cuadrado(-3, 'rojo')
print(cuadrado_2)
print(f'El area del cuadrado 2 es: {cuadrado_2.calcular_area()}')
print()

# validaciones cuando se modifica algun atributo
cuadrado_3 = Cuadrado(5, 'rojo')
print(cuadrado_3)
cuadrado_3.alto = 11
print(cuadrado_3)
print()

# MRO - Method Resolution Order 
# Permite conocer la jerarquía de clases
print(f'Jerarquia de las clases dentro de la clase Cuadrado: {Cuadrado.mro()}')
print()

print('Creacion Rectangulos'.center(15, '-'))

rectangulo_1 = Rectangulo(3, 4, 'violeta')
print(rectangulo_1)
print(f'Area de un rectangulo: {rectangulo_1.calcular_area()}')

# si se ingresa un numero menor a 0 o un num > 10
# el valor por defecto es 0
rectangulo_2 = Rectangulo(13, 24, 'violeta')
print(rectangulo_2)
print(f'Area de un rectangulo: {rectangulo_2.calcular_area()}')

# validaciones cuando se modifica algun atributo
rectangulo_3 = Rectangulo(1, 4, 'violeta')
print(rectangulo_3)
rectangulo_3.ancho = -4
print(rectangulo_3)
