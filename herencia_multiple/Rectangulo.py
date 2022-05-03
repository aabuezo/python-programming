from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return FiguraGeometrica.__str__(self) + ' ' + Color.__str__(self) + f' area: {self.calcular_area()}'


if __name__ == '__main__':
    print(Rectangulo.mro())
