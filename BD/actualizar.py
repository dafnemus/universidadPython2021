import psycopg2


conexion_2 = psycopg2.connect(user='dafne', password='dafne', host='localhost', port='5432',
database='dafne')


try:
    with conexion_2:
        with conexion_2.cursor() as cursor:
            sentencia = 'Update persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@gmail.com', 4)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion_2.close()


conexion_3 = psycopg2.connect(user='dafne', password='dafne', host='localhost', port='5432',
database='dafne')


try:
    with conexion_3:
        with conexion_3.cursor() as cursor:
            sentencia = 'Update persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Martinez', 'jmartinez@gmail.com', 6),
                ('Marta', 'Sanchez', 'msanchez@gmail.com', 7)
            )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion_3.close()
