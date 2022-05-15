# Sistemas numéricos
# Decimal
import math
from decimal import Decimal

a = 10
# Binario
a = 0b1010
# Hexadecimal
a = 0xA
print(f'a: {a}')

# convertir un entero incluyendo la base
a = int('23', 16)       # hexa
print(f'a: {a}')
a = int('10111', 2)     # binario
print(f'a: {a}')

# tipo float
a = 3.0
print(f'a: {a:.2f}')    # precision
# Notacion exponencial
a = 3e5
print(f'a: {a}')

# valores infinitos
infinito_positivo = float('inf')
print(f'infinito positivo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'infinito positivo: {infinito_negativo}')
print(f'es infinito: {math.isinf(infinito_negativo)}')

infinito_positivo = Decimal('Infinity')
print(f'infinito positivo: {infinito_positivo}')
print(f'es infinito: {math.isinf(infinito_positivo)}')

# tipo NaN (Not a Number)
a = float('NaN')
print(f'a: {a}')
print(f'es NaN: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'es NaN: {math.isnan(a)}')
