import psycopg2

# conexion a la base de datos, los valores son a modo de ejemplo.
conexion = psycopg2.connect(user='dafne', password='dafne', host='localhost', port='5432',
database='dafne')

print(conexion)

'''
# creacion de un cursor


# cerrar la conexion a la db
cursor.close()
conexion.close()
'''
# conexion con with
# base de datos
# sentencia = 'SELECT * FROM persona'
# recuperar columnas
# sentencia = 'SELECT id_persona, nombre FROM persona' 
# recuperar el registro de un id en particular
# sentancia = 'SELECT * FROM persona WHERE id_persona = 1'
# recuperar el registro de un id en particular a través de un parametro
# sentencia = 'SELECT * FROM persona WHERE id_persona = %s'

# %s = placeholder o parametro posicional

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Proporcione el id_persona que quiere recuperar: ')
            cursor.execute(sentencia, (id_persona,))
            # traer los registros de la db.
            # registros = cursor.fetchall()
            # recuperar un solo registro
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

