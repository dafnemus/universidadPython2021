class MiClase:

    variable_clase = 'Valor de variable clase'
    
    def __init__(self, variable_de_instancia) -> None:
        self.variable_de_instancia = variable_de_instancia

    @staticmethod # se asocia a la clase en si misma y no con los bojetos
    def metodo_estatico():  # No pueden acceder a variables de instancia directamente
        print(MiClase.variable_clase)


# Metodo statico
MiClase.metodo_estatico()

# acceso a una variable de instancia
mi_clase = MiClase('Variable de instancia')
print(mi_clase.variable_de_instancia)

# acceso a una variable de clase
# desde la clase misma
print(MiClase.variable_clase)

# desde un objeto
print(mi_clase.variable_clase)

# En el objeto 2 el valor de istancia puede no ser el mismo que el objeto 1
# pero la variable de clase seguira igual para ambos ojetos.
mi_clase_2 = MiClase('Otra variable de instancia')
print(mi_clase_2.variable_de_instancia)
print(mi_clase_2.variable_clase)


# variable de clase al vuelo(creada en cualquier momento)
MiClase.variable_de_clase_2 = 'Variable de clase 2'
print(MiClase.variable_de_clase_2)
print(mi_clase_2.variable_de_clase_2)
