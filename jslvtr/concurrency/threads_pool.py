import time
from concurrent.futures import ThreadPoolExecutor   # pool of threads with no target


def ask_user():
    user_input = input('Enter your name: ')     # Blocking operation
    greet = f'Hello, {user_input}'
    print(greet)


def complex_calculation():
    print('Started calculating...')
    [x**2 for x in range(20000000)]


# in Windows use: if __name__ == '__main__': !!!
start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time()-start}')


start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

# pool.shutdown()
print(f'Two thread total time: {time.time()-start}')
