class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona_1 = Persona('Pablo', 'Perez', 22)
print(f'Persona 1 se llama {persona_1.nombre}')

persona_2 = Persona('Marta', 'Gomez', 45)
print(f'persona 2, se llama {persona_2}')
