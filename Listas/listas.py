# Listas

lista = ['Juan', 'Ana', 'Ricardo', 'lila']
print(f'Esto es una lista: {lista}')

# Formas de acceso a cada item de la lista

# usando el indice
print(lista[0])
print(lista[1])
print(lista[2])

# usando el indice inverso
print(lista[-1])
print(lista[-2])
print(lista[-3])

# imprimir un rango
print(lista[0:3])

# Ir del inicio de la lista al indice(sin incluirlo)
print(lista[:3])

# Desde el indice indicado hasta el final
print(lista[1:])

# cambiar un valor de una lista
lista[1] = 'Pablo'
print(lista)

# iterar una lista
for i in lista:
    print(i)
