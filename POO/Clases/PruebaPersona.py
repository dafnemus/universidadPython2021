from Persona import Persona

# centro cadena y sumo 30 caracteres para rrellenar de izq a dcha.
print('Creacion de objetos'.center(30, '-'))
persona_1 = Persona('Juan', 'Perez', 33)
print(persona_1.mostrar_detalle())

# nombre del modulo
print(__name__)

print('Eliminacion de objetos'.center(30, '-'))
del persona_1
