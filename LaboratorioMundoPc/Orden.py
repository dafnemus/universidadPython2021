from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Computadora import Computadora


class Orden:
    contador_ordenes  = 0

    def __init__(self, lista_compus) -> None:
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.lista_compus = list(lista_compus)

    def agregar_compu(self, computadora):
        self.lista_compus.append(computadora)
    
    def __str__(self) -> str:
        resumen = ''
        for computadora in self.lista_compus:
            resumen += computadora
        
        return f'Orden n° {self.id_orden}: {resumen}'

if __name__ == '__main__':
    raton_1 = Raton('USB', 'Genius')
    teclado_1 = Teclado('Bluetooth', 'HP')
    monitor_1 = Monitor('Lenovo', 24)
    compu_1 = Computadora('c1', monitor_1, raton_1, teclado_1)
    raton_2 = Raton('USB', 'HP')
    teclado_2 = Teclado('Bluetooth', 'HP')
    monitor_2 = Monitor('HP', 24)
    compu_2 = Computadora('c2', monitor_2, raton_2, teclado_2)

    lista_compus_1 = [compu_1, compu_2]
    orden_1 = Orden(lista_compus_1)
    print(orden_1)


    lista_compus_2 = [compu_1]
    orden_2 = Orden(lista_compus_2)

    raton_3 = Raton('USB', 'HP')
    teclado_3 = Teclado('Bluetooth', 'HP')
    monitor_3 = Monitor('HP', 24)
    compu_3 = Computadora('c3', monitor_3, raton_3, teclado_3)

    orden_2.agregar_compu(compu_3)
    print(orden_2)
