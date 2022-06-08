import time
import random

from threading import Thread


counter = 0


def increment_counter():
    global counter
    counter += 1
    print(f'New counter value: {counter}')
    print('---------------------')


for x in range(10):
    t = Thread(target=increment_counter)
    t.start()

# Threads accesing a shared value, must be enqueued
# see non_lock_threads_2
