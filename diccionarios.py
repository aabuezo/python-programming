
# diccionarios
# key:value

dic = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(dic)
print(len(dic))

# acceder a un elemento
print(dic['IDE'])
# otra forma de recuperar un elemento
print(dic.get('OOP'))
# modificar elementos
# dic['IDE'] = 'ide'
# print(dic)
# recorrer elementos
for termino in dic:
    print(termino)
# otra forma
for clave, valor in dic.items():
    print(clave, valor)
# recuperar las claves
for clave in dic.keys():
    print(clave)
# recuperar los valores
for value in dic.values():
    print(value)

# comprobar existencia de algun elemento
print('IDE' in dic)
print('ide' in dic)

# agregar un elemento
dic['PK'] = 'Primary Key'
print(dic)

# remover un elemento
dic.pop('DBMS')
print(dic)

# limpiar el diccionario
dic.clear()
print(dic)

# eliminar el diccionario
del dic
# print(dic)

