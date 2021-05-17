# Ejercicio Padre/Madre asiste al juego

# Si el padre esta de vacaciones o día de descanso puede asistir al juego
# De lo contrario se encuentra ocupado.

madre_vacaciones = False
madre_dia_descanso = False

if madre_vacaciones or madre_dia_descanso:
    print('Mamá podrá asistir al juedo')
else:
    print('Mamá tiene que trabajar')

padre_vacaciones = False
padre_dia_descanso = True

if padre_vacaciones or padre_dia_descanso:
    print('Papá podrá asistir al juedo')
else:
    print('Papá tiene que trabajar')
