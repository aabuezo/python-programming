import random
import math
import time

from numba import jit


@jit(nopython=True)
def some_function(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 2)
    return z


start = time.time()
some_function(10000000)
end = time.time()
print(f"{(end-start)*1000} ms.")

start = time.time()
some_function(10000000)
end = time.time()
print(f"{(end-start)*1000} ms.")

start = time.time()
some_function(10000000)
end = time.time()
print(f"{(end-start)*1000} ms.")
