import psycopg2

# conexion a la base de datos, los valores son a modo de ejemplo.
conexion = psycopg2.connect(user='usuario', password='contraseña', host='localhost', port='5432',
database='base de datos')

print(conexion)

'''
# creacion de un cursor


# cerrar la conexion a la db
cursor.close()
conexion.close()
'''
# conexion con with
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            # traer los registros de la db.
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

