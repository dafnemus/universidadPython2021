# Conversión de números a string

numeros = {
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis',
    7: 'siete',
    8: 'ocho',
    9: 'nueve'
}


def convertir(numero: int) -> str:
    for key, value in numeros.items():
        if numero == key:
            print(f'numero:{numero} se escribe asi {value}')
        else:
            print('Valor fuera del rango')

valor = int(input('ingrese un numero del 1 al 9: '))
convertir(1)
convertir(valor)
