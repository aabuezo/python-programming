from clases.Persona import Persona


# herencia simple
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self._sueldo}'


if __name__ == '__main__':
    empleado1 = Empleado('Juan', 'Perez', 30, 5000)
    print(empleado1)