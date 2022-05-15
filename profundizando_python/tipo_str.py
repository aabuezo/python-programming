# las cadenas son inmutables
str1 = 'hola mundo'
str2 = str1.capitalize()
print(f'str1: {str2}, id: {hex(id(str2))}')
print(f'str1: {str1}, id: {hex(id(str1))}')
str1 += ' de python'
print(f'str1: {str1}, id: {hex(id(str1))}')


# metodo join
# se le debe pasar un iterable (lista, tupla, dict, etc)
csv = ','.join(['dato1', 'dato2', 'dato3'])
print(csv)

cadena = 'holamundo'    # una cadena tambien es un iterable
print('.'.join(cadena))


# split
cursos = 'Java Python Javascript HTML5 CSS3 C/C++'
lista_cursos = cursos.split() # por defecto toma el espacio en blanco
print(type(lista_cursos))
for curso in lista_cursos:
    print(curso)


# dar formato a un str
nombre = 'Juan'
edad = 28
sueldo = 5000
persona = ('Pedro', 35, 6500)
mensaje_con_formato = 'Mi nombre es %s, tengo %d años y mi sueldo es de $%.2f'%(nombre, edad, sueldo)
print(mensaje_con_formato)
mensaje_con_formato = 'Mi nombre es %s, tengo %d años y mi sueldo es de $%.2f'
print(mensaje_con_formato%persona)

# otras forma de dar formato a un str
mensaje = 'Nombre: {}, Edad: {}, Sueldo: {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)
mensaje = 'Edad: {1}, Nombre: {0}, Sueldo: {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)
mensaje = 'Nombre {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre: {persona[nombre]}'.format(persona=diccionario)
# print(mensaje)
mensaje = f'Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo:.2f}'
print(mensaje)
print(nombre, edad, sueldo, sep=', ')    # separador


# bytes
mensaje = b'Hola Mundo'
print(mensaje)
print(mensaje[0])
print(chr(mensaje[0]))


# convertir de str a bytes
string1 = 'Programación con Python'  # utf-8 por default: ú
print('string original:', string1)
bytes = string1.encode('utf-8')
print('bytes codificado:', bytes)
# convertir de bytes a str
string2 = bytes.decode('utf-8')
print('string decodificado:', string2)
print(string1 == string2)
print(f'id(string1): {id(string1)}')
print(f'id(string2): {id(string2)}')


# ver si un str contiene otro str
print('contiene Python: ', 'Python' in string1)
print('contiene python: ', 'python' in string1)
print('contiene python: ', 'python' in string1.lower())
print('string1 is lower:', string1.islower())
print('string1 is lower', string1.lower().islower())

# centrar un titulo
titulo = 'Pruebas con Python'
print(titulo.center(50, '-'))
print(titulo.ljust(50, '-'))
print(titulo.rjust(50, '-'))

# replace
string3 = string1.replace(' ', '_')
print(string3)

# strip: eliminar caracters al principio y al final
titulo = ' *** titulo *** '     # por default quita los espacios en blanco
print('cadena original:', titulo, len(titulo))
titulo = titulo.strip()
print('cadena modificada:', titulo, len(titulo))
titulo = '***titulo***'.rstrip('*')
print(titulo)
titulo = ' ***titulo*** '.strip().strip('*')
print(titulo)

# unpacking y partition
hora, _, minutos = '17:20'.partition(':') # devuelve una tupla
print(hora, _, minutos)
