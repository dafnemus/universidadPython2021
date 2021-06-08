# Ejercicio Laboratorio Cubo:
#   -Calcular el volumen de un cubo.
#   -los valores deberan ser ingresados por el usuario.
#   -Usar clases

class Cubo:
    def __init__(self, lado) -> None:
        self.lado = lado
    
    def calcular_volumen(self):
        return self.lado ** 3


lado = int(input('Ingrese el lado del cubo: '))

cubo_1 = Cubo(lado)
print(f'El valor del volumen del cubo 1 es {cubo_1.calcular_volumen()}')
