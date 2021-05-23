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

# saber la extensión de una lista
print(len(lista))

# agregar un elemento a la lista
lista.append('Laura')
print(lista)

# insertar un elemento en un indice en especifico
lista.insert(2, 'Martin')
print(lista)

# remover un elemento
lista.remove('Pablo')
print(lista)

# remover el ultimo elemento de la lista
lista.pop()
print(lista)

# eliminar segun indice
del lista[0]
print(lista)

# limpiar todos los elementos de nuestra lista
lista.clear()
print(lista)

# borrar la lista por completo
del lista
print(lista)
