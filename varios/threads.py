import threading
import time


def hola_mundo(nombre):
    print('Hola Mundo ' + nombre)
    time.sleep(5)


# https://www.youtube.com/watch?v=J9wOU5uWrjw
if __name__ == '__main__':
    thread = threading.Thread(target=hola_mundo, args=('Ale',))
    thread.start()
    thread.join()

    print('Hola mundo desde el thread principal')

