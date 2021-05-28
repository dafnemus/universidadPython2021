# Funciones


def mi_funcion() -> str:
    print('hola')


mi_funcion()

# argumentos y parametros
def saludar(nombre: str, apellido: str) -> str:
    print(f'Hola {nombre} {apellido}')


saludar('Lujan', 'Sproviero')

# uso del return
def sumar(a: int, b: int) -> int:
    return a + b


resultado = sumar(2, 7)
print(f'resultado de sumar: {resultado}')

# parametros por defecto
def sumar_v_2(a=0, b=0) -> int:
    return a + b


resultado = sumar_v_2()
print(f'resultado de sumar: {resultado}')
resultado = sumar_v_2(2, 8)
print(f'resultado de sumar: {resultado}')


# Argumentos variables
def listar_nombres(*nombres): # * = tupla
    for nombre in nombres:
        print(nombre)

listar_nombres('juan', 'carla', 'laila')

def listar_terminos(**terminos):
    for key, value in terminos.items():
        print(f'{key}: {value}')

listar_terminos(IDE='Integrated Development Environment', PK='Primary Key')
