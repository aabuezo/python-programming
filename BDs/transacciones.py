# TRANSACCIONES
# ejemplo sin with porque hace commit automaticamente
import psycopg2 as bd


conexion = bd.connect(
    user='usuario',
    password='password',
    host='localhost',
    port='5432',
    database='test_db'
)

try:
    # se recomienda el uso de with
    conexion.autocommit = False     # valor por default
    cursor = conexion.cursor()

    sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')  # error...
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()               # el autocommit = False nos obliga a usar commit()
    print('Termina la transaccion, se hizo commit')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error: {e}')
    print('Se realizo rollback de la transaccion.')
finally:
    conexion.close()
