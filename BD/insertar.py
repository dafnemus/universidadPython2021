import psycopg2


conexion_2 = psycopg2.connect(user='dafne', password='dafne', host='localhost', port='5432',
database='dafne')

# obtener varios registros:
# IN= in dica en varios registros
try:
    with conexion_2:
        with conexion_2.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido, email) VALUES(%s, %s,%s)'
            valores = ('Carlos', 'Lara', 'clara@gmail.com')
            cursor.execute(sentencia, valores)
            # guardar los cambios en la DB, con with se hace automaticamentes
            # conexion_2.commit()
            registros_nuevos = cursor.rowcount
            print(f'Registros nuevos: {registros_nuevos}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion_2.close()
