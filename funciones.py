# funciones

def sumar(a: int = 0, b: int = 0) -> int:
    return a + b


print(f'resultado = {sumar()}')
print(f'resultado = {sumar(3, 5)}')


# argumentos variables
# internamente *nombres se convierte en una tupla
# tambien se lo conoce como *args
def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)


listar_nombres('Juan', 'Karla', 'Maria', 'Ernesto')
listar_nombres('Laura', 'Carlos')


# argumentos variables tipo clave:valor
# tambien se lo conoce como **kwargs
# y el orden de llamada es el siguient
def listar_diccionario(**terminos):
    for clave, valor in terminos.items():
        print(f'{clave}: {valor}')


# la clave no lleva comillas y pude ser cualquier tipo de dato
listar_diccionario(IDE='Integrated Development Environment', PK='Primary Key')
listar_diccionario(DBMS='Database Management System')
# y el orden de llamada es el siguiente
# def listar_diccionario(nombre, *nombres, **terminos):


# pasar una lista a una funcion
def listar_nombres(lista_nombres):
    for nombre in lista_nombres:
        print(nombre, end=' ')


nombres = ['Juan', 'Karla', 'Guillermo']
listar_nombres(nombres)
listar_nombres('Carlos\n')


# funciones recursivas
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = 5
print(f'factorial({numero}) = {factorial(numero)}')
