class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return f'Empleado: {self.nombre}, sueldo: ${self.sueldo}'
