# Uso de try/except para manejar excepciones.
from NumerosIdenticosException import NumerosIdenticosException
resultado = None


# Captura generica de un error 
try:
    a = '10'
    b = 0
    resultado = a / b
except Exception as e:
    print(f'Ocurrió el siguiente error: {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')


# De excepciones especificas a genericas
try:
    print('DIVISION, ingrese dos numeros')
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('Números idénticos')
    resultado = a / b
except ZeroDivisionError as zde:
    print(f'ZDE-Ocurrió el siguiente error: {zde}')
except TypeError as te:
    print(f'TE-Ocurrió el siguiente error: {te}')
except Exception as e:
    print(f'E-Ocurrió el siguiente error: {e}')
else:  # solo si no hubo ningún error
    print('EJECUCIÓN EXITOSA')
finally:  # se ejecutará siempre
    print('Ejecución finalizada')

print(f'Resultado: {resultado}')
print('Continuamos...')
