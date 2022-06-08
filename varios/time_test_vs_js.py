import time
from numba import jit


@jit(nopython=True)
def time_test():
    doscientos_millones = 200000000
    for i in range(doscientos_millones):
        pass


start = time.time()
time_test()
end = time.time()
print(f'El proceso tardo: {(end-start)*1000} ms.')
