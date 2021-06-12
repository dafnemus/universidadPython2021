from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__():
        return f'Cuadrado {self.color}'

    def calcular_area(self):
        return self.alto * self.ancho
