class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre  # Encapsulamiento = _
        self._apellido = apellido
        self.edad = edad

    @property  # permite acceder a un metodo como si fuese un atribuot
    def apellido(self):
        return self._apellido

    # metodo Get
    def get_nombre(self):
        return self._nombre
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    def mostrar_detalle(self):
        return f'Persona: {self._nombre} {self._apellido}'

persona_1 = Persona('Pablo', 'Perez', 22)
print(f'Persona 1 se llama {persona_1._nombre}')

# hay que evitar lo siguiente:
print(persona_1._nombre)
# recomendado:
# 1_ usar un metodo get
print(persona_1.get_nombre())
# 2_ con property
print(persona_1.apellido)

# setter:
persona_1.apellido = 'Suarez'
print('Edad setteada', persona_1.apellido)


persona_2 = Persona('Marta', 'Gomez', 45)
print(f'persona 2, se llama {persona_2.get_nombre()}')

persona_1.mostrar_detalle()
persona_2.mostrar_detalle()
