# ABC = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):    # clase abstracta
    def __init__(self, alto, ancho):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

    @property
    def alto(self):
        return self._alto

    # solo lectura
    # @alto.setter
    # def alto(self, alto):
    #     if self._validar_valor(alto):
    #         self._alto = alto
    #     else:
    #         self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    # solo lectura
    # @ancho.setter
    # def ancho(self, ancho):
    #     if self._validar_valor(ancho):
    #         self._ancho = ancho
    #     else:
    #         self._ancho = 0

    def __str__(self):
        return f'alto: {self._alto}, ancho: {self._ancho}'

    def _validar_valor(self, valor):
        return True if 0 < valor else False

    @abstractmethod     # metodo abstracto
    def calcular_area(self):
        pass
