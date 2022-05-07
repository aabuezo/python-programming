# uso de with
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
            sentencia = 'SELECT * FROM personas WHERE id_persona = %s'
            id_persona = 2
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchall()   # o fetchone()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
