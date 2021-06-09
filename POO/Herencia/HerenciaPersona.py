class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'''
            Nombre: {self.nombre}
            Edad: {self.edad}
        '''

class Empleado(Persona):
    def __init__(self, nombre, edad, salario, puesto) -> None:
        super().__init__(nombre, edad)
        self.salario = salario
        self.puesto = puesto

    def __str__(self) -> str:
        return f'''
            {super().__str__()}
            Salario: ${self.salario}
            Puesto: {self.puesto}
        '''
