from collections import deque


friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


# this is not a generator anymore, because it receives data
# it is now known as a COROUTINE
def friend_upper():
    while friends:  # could be waiting sth from internet
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


# def greet(g):
#     g.send(None)
#     while True:             # running for ever
#         greeting = yield    # suspended
#         g.send(greeting)


# the function above can be replaced by
def greet(g):
    yield from g    # can be used to send and receive data, but nobody likes it


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('')
greeter.send('Hello')
print('Hello, world! Multitasking...')  # multitasking
greeter.send('How are you,')
