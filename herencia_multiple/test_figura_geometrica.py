from Cuadrado import Cuadrado
from herencia_multiple.Rectangulo import Rectangulo


print('Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=-5, color='rojo')
print(f'Area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(alto=3, ancho=5, color='azul')
print(f'Area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
