# Generadores
# es una funcion que retorna una secuencia de valores de a uno a la vez
# se usa yield en vez de return

def generador():
    for num in range(1, 4):
        yield num


# Consumimos el generador a demanda
gen = generador()
print(type(gen))
# con cada llamada consumimos un valor
try:
    print(next(gen))
    print(next(gen))
    print(next(gen))        # aqui se termina el generador
    print(next(gen))        # arroja StopIteration
except StopIteration:
    print(f'Se termino lo que se daba...')

# hay que volver a llamar al generador para usarlo de nuevo
for valor in generador():
    print(f'valor: {valor}')

# otra forma con while true
gen = generador()
while True:
    try:
        valor = next(gen)
        print(f'valor generado: {valor}')
    except StopIteration as e:
        print('Se termino la iteracion')
        break   # salgo!

