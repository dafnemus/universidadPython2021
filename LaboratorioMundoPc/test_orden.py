from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Computadora import Computadora
from Orden import Orden


raton_1 = Raton('USB', 'Genius')
teclado_1 = Teclado('Bluetooth', 'HP')
monitor_1 = Monitor('Lenovo', 24)
compu_1 = Computadora('c1', monitor_1, raton_1, teclado_1)

raton_2 = Raton('USB', 'HP')
teclado_2 = Teclado('Bluetooth', 'HP')
monitor_2 = Monitor('HP', 24)
compu_2 = Computadora('c2', monitor_2, raton_2, teclado_2)

raton_3 = Raton('USB', 'HP')
teclado_3 = Teclado('Bluetooth', 'HP')
monitor_3 = Monitor('HP', 24)
compu_3 = Computadora('c3', monitor_3, raton_3, teclado_3)

lista_compus_1 = [compu_1, compu_3]
orden_1 = Orden(lista_compus_1)
print(f'Orden: {orden_1.id_orden}'.center(30, '-'))
print(orden_1)

lista_compus_2 = [compu_1, compu_2]
orden_2 = Orden(lista_compus_2)
print(orden_2)
orden_2.agregar_compu(compu_3)
print(f'Orden: {orden_2.id_orden}'.center(30, '-'))
print(orden_2)
