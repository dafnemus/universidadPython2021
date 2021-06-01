# Distintos tipos de datos como argumentos para una sola funcion

def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Carlos', 'Carla', 'Juana']

# flexibilidad de Python
desplegar_nombres(nombres)
desplegar_nombres('carlos')
desplegar_nombres((1, 2))
desplegar_nombres([1, 2])


# Funciones recursivas

# factoreo de 5:
# 5!= 5 * 4 * 3 * 2 * 1 = 120
n = 5
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(f'El factoral de {n} es igual a {factorial(n)}')
