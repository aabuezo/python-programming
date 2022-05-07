# INSERT 1
import psycopg2


conn = psycopg2.connect(
    user='usuario',
    password='password',
    host='localhost',
    port='5432',
    database='test_db'
)

try:
    with conn:
        with conn.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            # executemany necesita una tupla de tuplas
            valores = (
                ('Marcos', 'Cantu', 'mcantu@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzalez', 'mgonzalez@mail.com'))
            cursor.executemany(sentencia, valores)
            # conexion.commit()     # no hace falta por el with
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
