# Operadores

from os import PRIO_PGRP


operando_a = 3
operando_b = 6

print('SUMA')
suma = operando_a + operando_b
print(f'{operando_a} + {operando_b} = {suma}')

print('RESTA')
resta = operando_a - operando_b
print(f'{operando_a} - {operando_b} = {resta}')

print('MULTIPLICACIÓN')
multiplicacion = operando_a * operando_b
print(f'{operando_a} * {operando_b} = {multiplicacion}')

print('DIVISIÓN')
division = operando_a / operando_b
print(f'{operando_a} / {operando_b} = {division}')

print('DIVISIÓN EXACTA')
division_exacta = operando_a // operando_b
print(f'{operando_a} // {operando_b} = {division_exacta}')

print('POTENCIA')
potencia = operando_a ** operando_b
print(f'{operando_a} ** {operando_b} = {potencia}')

print('MÓDULO')
modulo = operando_a % operando_b
print(f'{operando_a} % {operando_b} = {modulo}')
