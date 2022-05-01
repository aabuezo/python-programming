# tuplas: inmutables
# al igual que las listas, se respeta el orden de los elementos

frutas = ('naranja', 'platano', 'guayaba')
print(frutas)
print(len(frutas))
print(frutas[0:1])
for fruta in frutas:
    print(fruta, end=' ')

frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas)

# no se pueden usar: append, insert ni remove
# si se puede borrar la tupla completamente
del frutas
#print(frutas)

tupla = (1, 13, 8, 5, 2, 8, 11)
lista = [i for i in tupla if i <= 5]
print(lista)


