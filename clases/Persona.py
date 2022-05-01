class Persona:
    """
    Docstring:
    clase basica
    """
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property # se puede acceder al metodo como si fuera un atributo - getter
    def nombre(self):
        #print('getter...')
        return f'Nombre: {self._nombre}'

    # si comentamos el setter, el atributo queda de solo lectura
    @nombre.setter
    def nombre(self, nombre):
        #print('setter...')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # metodo destructor
    def __del__(self):
        print(f'Eliminando persona: {self._nombre} {self._apellido}')

    def __str__(self):
        return f'Persona: {self._nombre} {self._apellido}, Edad: {self._edad}'


if __name__ == '__main__':
    print(type(Persona))
    persona1 = Persona('Juan', 'Perez', 26)
    print(persona1.nombre)

    persona2 = Persona('Karla', 'Gomez', 30)
    print(persona2.nombre)
    persona2.nombre = 'Karlita'
    print(persona2.nombre)

    print(__name__)
