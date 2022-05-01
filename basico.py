# comentario simple
miVariable = "Hola desde Python"
print(miVariable)
print(id(miVariable))

miVariable = 1 > 2
if miVariable:
    print("1 es mayor que 2")
else:
    print("1 es menor que 2")

miVariable = 5
if 0 < miVariable < 10:
    print(f'mi variable: {miVariable}')

""" Doctring o comentario para documentar """
a = 1
a += 2
print(a)

while a > 0:
    print(a)
    a -= 1
else:
    print('Fin del ciclo while')

cadena = 'Holanda'
for letra in cadena:
    print(letra)
    if letra == 'a':
        break

for i in range(10):
    print(f'i: {i}')
