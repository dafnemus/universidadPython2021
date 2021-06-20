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
