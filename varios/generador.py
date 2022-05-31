def frutas():  # funcion generador
    yield 'manzana'
    print('hola')
    yield 'banana'
    yield 'pera'


def cosas():
    yield "espada"
    yield "auto"
    yield from frutas()
    yield "celular"


f = frutas()
print(next(f))
print(next(f))
print(next(f))

print()

c = cosas()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
try:
    print(next(c))
except StopIteration:
    print('stop...')
