# Diccionarios 

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

# largo
print(len(diccionario))

# acceder a un elemento
print(diccionario['OOP'])

# acceder a un elemento con get
print(diccionario.get('IDE'))

# modificacion de elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

# iteracion
# acceder a las KEYS
for key in diccionario:
    print(key)

# otra forma de acceder a las KEYS
for key in diccionario.keys():
    print(key)

# acceder a los y a las keys valores con items
for key, value in diccionario.items():
    print(key, value)

# acceder solo a los valores
for value in diccionario.values():
    print(value)

# comprobar si existe un elemeto
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('IDE')
print(diccionario)
