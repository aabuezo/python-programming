import time
from threading import Thread


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


def run_functions_without_treads():
    time_func(ask_user)
    time_func(complex_calculation)


def run_functions_with_threads():
    thread1 = Thread(target=complex_calculation)
    # thread2 = Thread(target=complex_calculation)  # tarda 4 veces mas!!
    thread2 = Thread(target=ask_user)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == '__main__':
    time_func(run_functions_without_treads)
    time_func(run_functions_with_threads)
