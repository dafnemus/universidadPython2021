import psycopg2 as bd


conexion_2 = bd.connect(user='dafne', password='dafne', host='localhost', port='5432',
database='dafne')


try:
    conexion_2.autocommit = False

    cursor = conexion_2.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    valores = ('Lucas', 'Musante', 'lmusante@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Mili', 'Lopez', 'mlopez@mail.com', 2)
    cursor.execute(sentencia, valores)

    conexion_2.commit()
    print('Transacción finalizada, cambios guardados')
except Exception as e:
    conexion_2.rollback()
    print(f'Ocurrió un error, se produjo rollback: {e}')
finally:
    conexion_2.close()


# con WITH:
'''
try:
    with conexion_2:
        with conexion_2.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('Lucas', 'Musante', 'lmusante@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Mili', 'Lopez', 'mlopez@mail.com', 2)
            cursor.execute(sentencia, valores)
            print('Transacción finalizada, cambios guardados')
except Exception as e:
    print(f'Ocurrió un error, se produjo rollback: {e}')
finally:
    conexion_2.close()
'''
