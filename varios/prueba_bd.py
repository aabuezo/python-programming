import mysql.connector as mysql

conn = mysql.connect(
    host='localhost',
    user = 'usuario',
    password = 'password',
    database = 'testdb'
)

print(conn)

my_cursor = conn.cursor()
my_cursor.execute('SELECT * FROM testdb.personas')
registros = my_cursor.fetchall()
print(registros)
# for x in my_cursor:
#     print(x)

my_cursor.close()
# conn.close()


# with
try:
    with conn:
        with conn.cursor() as cursor:
            sentencia = 'SELECT * FROM personas'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'ocurrio un error: {e}')


