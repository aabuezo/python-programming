# comes from receiving_through_yield_2.py
from collections import deque
from types import coroutine


friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:  # could be waiting sth from internet
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g     # yield from g
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')  # multitasking
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
