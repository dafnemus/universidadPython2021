# Tuplas

tupla_de_frutas = ('Naranja', 'Manzana', 'Banana')
print(tupla_de_frutas)

# largo de una tupla
print(len(tupla_de_frutas))

# acceder a un elemento indices
print(tupla_de_frutas[1])

# navegacion inversa indices
print(tupla_de_frutas[-1])

# acceder a un rango de valores
print(tupla_de_frutas[0:2])

# recorrer elementos
for fruta in tupla_de_frutas:
    print(fruta, end='//')

# cambiar el valor de una tupla conversiones
fruta_lista = list(tupla_de_frutas)
fruta_lista[1] = 'Pera'
frutas = tuple(fruta_lista)
print('\n', frutas)
