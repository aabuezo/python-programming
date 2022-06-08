import time
from concurrent.futures import ProcessPoolExecutor


def time_func(func):
    start = time.time()
    func()
    end = time.time()
    print(f'{func.__name__}: {end-start}')


def ask_user():
    user_input = input('Enter your name: ')     # Blocking operation
    greet = f'Hello, {user_input}'
    print(greet)


def complex_calculation():
    print('Started calculating...')
    [x**2 for x in range(20000000)]


def run_functions_without_processes():
    time_func(ask_user)
    time_func(complex_calculation)


# run_functions_without_processes()

start = time.time()

with ProcessPoolExecutor(max_workers=4) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

end = time.time()
time_dif = end - start
print(f'Two processes total time: {time_dif}')

