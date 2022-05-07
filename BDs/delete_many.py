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
            sentencia = 'DELETE FROM personas WHERE id_persona IN %s'
            entrada = input('Ingrese id_persona(s) (separados por coma): ')
            valores = (tuple(entrada.split(',')) ,)
            cursor.execute(sentencia, valores)      # no hace falta executemany para delete
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
