# paralelismo REAL
import time
import threading
from multiprocessing import Process


def countdown(number):
    while number > 0:
        number -= 1


if __name__ == '__main__':
    start = time.time()

    count = 10**9

    t1 = Process(target=countdown, args=(count,))
    t2 = Process(target=countdown, args=(count,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'tiempo transcurrido: {time.time() - start}')

