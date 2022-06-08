import time
from numba import jit
from multiprocessing import Process


def time_func(func):
    start = time.time()
    func()
    end = time.time()
    print(f'{func.__name__}: {end-start}')


@jit(nopython=True)
def complex_calculation():
    print('Started calculating...')
    [x**2 for x in range(50000000)]


print("Un solo proceso".center(50, '*'))
time_func(complex_calculation)


CORES = 4
print(f"{CORES} procesos".center(50, '*'))
start = time.time()

processes = []
for process in range(CORES):
    processes.append(Process(target=complex_calculation))

# print(processes)

for process in processes:
    process.start()
    # process.join()    # si lo dejo aca, corren uno atras del otro - 28 seg

for process in processes:
    process.join()

end = time.time()
time_dif = end - start
print(f'{len(processes)} processes total time: {time_dif}')


