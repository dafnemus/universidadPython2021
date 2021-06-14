from Ejercicios.ContadorDeObjetos.Persona import Persona

persona_1 = Persona('Juan', 28)
print(persona_1)
persona_2 = Persona('Karla', 30)
print(persona_2)
persona_3 = Persona('Eduardo', 25)
print(persona_3)
print(f'Valor contador personas: {Persona.contador_personas}')
