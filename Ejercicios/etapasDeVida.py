# Ejercicio etapas de vida:

# Proporcionar tu edad y determinar lo siguiente:
#   - 0 a 10 = infancia
#   - 11 a 20 = adolescencia
#   - 21 a 30 = joven-adulto
#   - 31+ = adulto

def determinar_etapa_vida(edad):
    etapa = None
    if 0 <= edad <= 10:
        etapa = 'Infancia'
    elif 11 <= edad <= 20:
        etapa = 'adolescencia'
    elif 21 <= edad <= 30:
        etapa = 'Joven adulto'
    elif edad > 30:
        etapa = 'Adulto'
    else:
        etapa = 'No existe'
    print(f'Su edad: {edad} corresponde a la {etapa}')

determinar_etapa_vida(2)
determinar_etapa_vida(21)
determinar_etapa_vida(12)
determinar_etapa_vida(32)
