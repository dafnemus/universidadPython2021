from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))


empleado_1 = Empleado('Juan', 30000)
imprimir_detalles(empleado_1)


gerente_1 = Gerente('Camila', 300000, 'Finanzas')
imprimir_detalles(gerente_1)
