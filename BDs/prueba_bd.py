# conexion basica a postgres
import psycopg2


conexion = psycopg2.connect(
    user='user',
    password='pass',
    host='serverlx',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM personas ORDER BY id_persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()
