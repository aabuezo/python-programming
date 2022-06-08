def greet():
    friend = yield
    print(f'Hello, {friend}')


g = greet()
g.send(None)    # priming the generator (gets up to yield)
g.send('Charlie')
