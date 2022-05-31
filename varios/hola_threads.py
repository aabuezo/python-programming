from threading import Thread


def saludar(thread_id):
    print(f'Hola, soy el thread {thread_id}!')


threads = [Thread(target=saludar, args=(thread_id,)) for thread_id in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()


