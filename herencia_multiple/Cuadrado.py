from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return FiguraGeometrica.__str__(self) + ' ' + Color.__str__(self) + f' area: {self.calcular_area()}'


if __name__ == '__main__':
    # con ABC se modifica el method resolution order
    print(Cuadrado.mro())

