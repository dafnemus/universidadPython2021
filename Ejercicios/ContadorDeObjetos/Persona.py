# Ejercicio contador de personas

class Persona:
    '''
        La clase se va a llamar persona, por cada objeto de tipo persona que creemos, vamos a asignarle un identificador único y para ello definir una variable de clase.
    '''

    contador_personas = 0
    
    @classmethod
    def contar_personas(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad) -> None:
        self.id_persona = Persona.contador_personas()
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'''
            Persona {self.id_persona}:
            Nombre: {self.nombre}, Edad: {self.edad}
        '''
