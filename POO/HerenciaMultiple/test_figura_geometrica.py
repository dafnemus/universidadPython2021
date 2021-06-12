from POO.HerenciaMultiple.Rectangulo import Rectangulo
from POO.HerenciaMultiple.Cuadrado import Cuadrado


cuadrado_1 = Cuadrado(10, 'verde')
print(f'El area del cuadrado 1 es: {cuadrado_1.calcular_area()}')
print(cuadrado_1)
print()

cuadrado_2 = Cuadrado(3, 'rojo')
print(f'El area del cuadrado 2 es: {cuadrado_2.calcular_area()}')
print(cuadrado_2)
print()

# MRO - Method Resolution Order 
# Permite conocer la jerarquía de clases
print(f'Jerarquia de las clases dentro de la clase Cuadrado: {Cuadrado.mro()}')
print()

rectangulo_1 = Rectangulo(3, 4, 'violeta')
print(rectangulo_1)
print(f'Area de un rectangulo: {rectangulo_1.calcular_area()}')
