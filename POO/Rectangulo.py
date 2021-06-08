class Rectangulo:
    '''
    Calcular el area de un rectangulo
    '''
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.altura * self.base


rectangulo_1 = Rectangulo(5, 8)
rectangulo_1.calcular_area()
