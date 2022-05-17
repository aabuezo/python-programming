from dataclasses import dataclass
from typing import ClassVar


# para clases directas sin mucha funcionalidad
@dataclass(eq=True, frozen=True)    # inmutable
class Domicilio:
    calle: str
    numero: int = 0


# @dataclass agrega __init__ y __repr__
@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'El atributo nombre vino vacio')


domicilio1 = Domicilio('Saturno', 15)
domicilio2 = None
persona1 = Persona('Juan', 'Perez', domicilio1)
print(f'{persona1!r}')      # !r manda a llamar a __repr__ directamente (sin pasar por __str__)

# variable de clase
print(f'variable de clase: {Persona.contador_personas}')

# variables de instancia
print(f'variables de instancia: {persona1.__dict__}')

# persona sin datos
persona2 = Persona('Karla', '', domicilio2)
print(persona2)

# eq
print(f'son iguales? {persona1 == persona2}')   # eq=True

# agregar a coleccion (set) o dict que necesita que sean inmutables (por el hash)
conjunto = {persona1, persona2}     # frozen=True
print(conjunto)
