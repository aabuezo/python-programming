# suma de cuadrados
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

# ejemplo con listas
# util si no sabemos cuantos elementos contiene una lista...
# porque se recuperan a demanda
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)  # se usan parentesis
print(next(generador))
print(next(generador))

# list comprehension
lista_pares = [num for num in range(10) if num > 1 if num%2 == 0]
print(lista_pares)
