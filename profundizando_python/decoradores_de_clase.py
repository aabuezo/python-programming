# Decoradores de Clase
# Permiten transformar una clase de manera programatica
# es metaprogramacion
import inspect


def decorador_repr(cls):
    print('se ejecuta el decorador de clase')
    print(f'recibimos el objeto de la clase: {cls.__name__}')

    # vars regresa el dict de la clase
    atributos = vars(cls)
    # for nombre, valor in atributos.items():
    #     print(nombre, valor)

    # revisamos si se sobreescribio el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'La clase {cls.__name__} no ha sobreescrito el metodo __init__()')
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del metodo init: {firma_init}')
    # recuperamos los parametros
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros __init__(): {parametros_init}')

    # revisamos si cada parametro tiene un metodo property asociado
    for param in parametros_init:
        # property es un valor del tipo built-in para preguntar si se esta utilizando
        # el decorador de property
        es_property = isinstance(atributos.get(param), property)
        if not es_property:
            raise TypeError(f'No existe un método property para el parámetro: {param}')

    # crear el metodo repr dinamicamente
    def metodo_repr(self):
        # obtenemos el nombre de la clase
        nombre_clase = self.__class__.__name__
        # obtenemos los nombres de las propiedades y sus valores dinamicamente
        # expresion generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # lista del generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        # creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos de repr: {argumentos}')
        # creamos la forma del método repr, sin su nombre
        resultado = f'{nombre_clase}({argumentos})'
        return resultado

    # agregar dinamicamente el metodo_repr a la clase
    setattr(cls, '__repr__', metodo_repr)

    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('se ejecuta __init__')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad


persona1 = Persona('Juan', 'Perez', 28)
print(persona1)
persona2 = Persona('Karla', 'Gomez', 37)
print(persona2)


# vemos que se agregaron los metodos nombre, apellido, edad y __repr__ a la clase
print(dir(Persona))

# vemos el código sobreescrito del método __repr__
codigo_repr = inspect.getsource(Persona.__repr__)
print(codigo_repr)
