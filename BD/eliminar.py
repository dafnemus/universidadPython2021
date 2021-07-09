import psycopg2


conexion_2 = psycopg2.connect(user='dafne', password='dafne', host='localhost', port='5432',
database='dafne')


try:
    with conexion_2:
        with conexion_2.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Proporcione el id persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion_2.close()
