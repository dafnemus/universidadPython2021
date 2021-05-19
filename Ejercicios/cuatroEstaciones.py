# Ejercicio Estaciones del Año:
#   -PRIMAVERA, VERANO, OTONO, INVIERNO.
# Proporcionar un mes y determinar su estacion correspondiente.

meses = ['enero', 'febrero','marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

estacion = None

# segun hemisferio SUR
def determinar_estacion_año(mes: str) -> str:
    for m in range(len(meses)):
        if meses[m] == mes:
            if m <= 1 or m == 11:
                estacion = 'VERANO'
                print(f'Es {estacion} en el mes de {mes}')
            elif m == 2 or m <= 4:
                estacion = 'OTOÑO'
                print(f'Es {estacion} en el mes de {mes}')
            elif m == 5 or m <= 7:
                estacion = 'INVIERNO'
                print(f'Es {estacion} en el mes de {mes}')
            else:
                estacion = 'PRIMAVERA'
                print(f'Es {estacion} en el mes de {mes}')



determinar_estacion_año('enero')
determinar_estacion_año('julio')
determinar_estacion_año('mayo')
determinar_estacion_año('octubre')
