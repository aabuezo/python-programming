# conexion basica a postgres
import psycopg2


conexion = psycopg2.connect(
    user='usuario',
    password='password',
    host='localhost',
    port='5432',
    database='test_db'
)

print(conexion)
cursor = conexion.cursor()
sentencia = 'SELECT * FROM personas ORDER BY id_persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(f'registros (lista): {registros}')
for registro in registros:
    print(registro)

cursor.close()
conexion.close()
print(conexion)

