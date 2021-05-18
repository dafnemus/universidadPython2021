# Ejercicio Edad dentro del rango 20'-30'

edad_usuario = int(input('Ingrese su edad? '))

def rangear_edad(edad: int) -> str:
    if edad >= 20 and edad < 40:
        print('Tu edad esta en el rango')
        if edad >= 20 and edad < 30:
            print('Estas dentro de los 20')
        elif edad >= 30 and edad < 40:
            print('Estas dentro de los 30')
    else:
        print('Tu edad esta fuera del rango')


rangear_edad(edad_usuario)
