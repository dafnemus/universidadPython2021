from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

    def calcular_area(self):
        return self.alto * self.ancho
