# Ejecicio Califica tu día
# Preguntar al usuario que califique su día del 1 al 10.

calificacion = int(input('Cómo estuvo tu día (1 al 10)?: '))

if 0 > calificacion <= 10:
    print(f'Mi día estuvo de: {calificacion}')
else:
    print('La calificación no coincide con los parametros')
