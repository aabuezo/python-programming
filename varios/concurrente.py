import time
import logging

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def super_task(a, b):
    time.sleep(1)
    logging.info(f'terminamos la tarea compleja {a} - {b}\n')


def hola():
    print('hola desde un thread dentro de un pool')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(super_task, 1, 2)
        executor.submit(super_task, 3, 4)

        executor.submit(super_task, 5, 6)
        executor.submit(super_task, 7, 8)

        executor.submit(super_task, 9, 10)
        executor.submit(super_task, 11, 12)

        executor.submit(super_task, 13, 14)
        executor.submit(hola)
