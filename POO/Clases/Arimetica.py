class Arimetica:
    '''
    operaciones de suma y resta
    '''
    def __init__(self, operando_a, operando_b) -> None:
        self.operando_a = operando_a
        self.operando_b = operando_b

    def sumar(self):
        return self.operando_a + self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b


operacion_1 = Arimetica(3, 5)
print(f'{operacion_1.operando_a}+{operacion_1.operando_b} = {operacion_1.sumar()}')
print(f'{operacion_1.operando_a}-{operacion_1.operando_b} = {operacion_1.restar()}')
