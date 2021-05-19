# ciclo for

cadena = 'hola mundo'

for letra in cadena:
    print(letra)
else:
    print(f'fin palabra, {cadena}')

# Range
for i in range(6):
    print(i)

# continue
for i in range(8):
    if i % 2 != 0:
        continue
    print(f'valor: {i}')
