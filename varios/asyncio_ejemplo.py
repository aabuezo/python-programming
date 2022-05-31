from asyncio import run, gather, sleep
import time


async def subir_foto():
    print('s: subiendo byte 1')
    await sleep(0)      # en lugar de yield
    print('s: subiendo byte 2')
    await sleep(0)
    print('s: subiendo byte 3')


# @asyncio.coroutine
async def twitter():
    print('t: leyendo a roberto')
    await sleep(0)
    # yield
    print('t: discutiendo con roberto')
    await sleep(0)
    # yield
    print('t: postear foto')
    # time.sleep(5)   # simula una operacion de I/O
    # yield
    # yield from subir_foto()
    await subir_foto()
    print('t: indignandome por politica')


async def estudiar():
    print('e: leyendo el material')
    await sleep(0)
    # yield
    print('e: armando resumen')
    await sleep(0)
    # yield
    print('e: leyendo resumen')     # sin pausa en el medio
    print('e: memorizando resumen')
    await sleep(0)
    # yield
    print('e: llorando')


# def loop(tareas):   # lista de tareas
#     while tareas:
#         actual = tareas.pop(0)  # la primer tarea
#         print(f'actual: {actual}')
#         try:
#             next(actual)
#             tareas.append(actual)
#         except StopIteration:
#             pass


# loop([twitter(), estudiar()])


async def main():
    print('inicio del programa')
    # await asyncio.gather([twitter(), estudiar()])
    await gather(twitter(), estudiar())
    print('fin del programa')


# async.run(main())
run(main())
