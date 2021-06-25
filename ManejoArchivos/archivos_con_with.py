'''
Forma básica:
with open('prueba.txt', 'r', encoding='utf8') as f:
    print(f.read())
'''

from ManejoArchivos.ManejoArchivos import ManejoArchivos


with ManejoArchivos('prueba.txt') as f:
    print(f.read())
