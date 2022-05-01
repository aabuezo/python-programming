# listas

nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
print(nombres)
print(nombres[0])
print(nombres[-1])
print(nombres[1:3])
print(nombres[2:])
nombres[3] = 'Ivone'

# recorrer una lista
for nombre in nombres:
    print(nombre)
# imprimir la longitud de una lista
print(len(nombres))

# agregar un elemento al final
nombres.append('Lorenzo')

# insertar un elemento
nombres.insert(1, 'Octavio')
print(nombres)

# eliminar un elemento
nombres.remove('Octavio')
print(nombres)

# quitar el ultimo elemento
nombres.pop()
print(nombres)

# borrar un elemento con el indice
del nombres[0]
print(nombres)

# limpiar el elemento
nombres.clear()
print(nombres)

# eliminar la lista
del nombres
#print(nombres)

