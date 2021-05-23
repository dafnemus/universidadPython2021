# Set

planetas_set = {'Marte', 'Mercurio', 'Venus'}

# impresion desordenada
print(planetas_set, type(planetas_set))

# largo de elementos
planetas_set(len(planetas_set))

# revisar si un elemento esta presente
print( 'Marte' in planetas_set)

#  agregar elementos
planetas_set.add('Tierra')
print(planetas_set)

# No soporta lementos duplicados
planetas_set.add('Tierra')
print(planetas_set)

# eliminar elementos
planetas_set.remove('Mercurio')
print(planetas_set)

# elimina elemntos sin arrojar error sino encuentra el elemento
planetas_set.discard('Mercur')
