import psycopg2

# conexion a la base de datos, los valores son a modo de ejemplo.
conexion = psycopg2.connect(user='usuario', password='contraseña', host='localhost', port='5432',
database='base de datos')

print(conexion)

# creacion de un cursor
cursor = conexion.cursor()

sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
# traer los registros de la db.
registros = cursor.fetchall()
print(registros)

# cerrar la conecion a la db
cursor.close()
conexion.close()
