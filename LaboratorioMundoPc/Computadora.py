from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, raton, teclado) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    def __str__(self) -> str:
        return f''''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    raton_1 = Raton('USB', 'Genius')
    teclado_1 = Teclado('Bluetooth', 'HP')
    monitor_1 = Monitor('Lenovo', 24)
    compu_1 = Computadora('c1', monitor_1, raton_1, teclado_1)
    print(compu_1)
    raton_2 = Raton('USB', 'HP')
    teclado_2 = Teclado('Bluetooth', 'HP')
    monitor_2 = Monitor('HP', 24)
    compu_2 = Computadora('c2', monitor_2, raton_2, teclado_2)
    print(compu_2)
