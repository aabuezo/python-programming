# funciones built-in que usan generators

# filter()
friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda x: x.startswith('R'), friends) # arg 1: function that returns True/False

print(next(start_with_r))
print(next(start_with_r))

another_starts_with_r = (f for f in friends if f.startswith('R'))   # similar - faster - more pythonic
print(list(another_starts_with_r))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


print(list(my_custom_filter(lambda x: x.startswith('R'), friends)))


# map()
friends_lower = map(lambda x: x.lower(), friends)   # generator
print(next(friends_lower))


# any() and all()
if any(friends):        # any is True
    print("You have at least one friend")

if not all(friends) == 'Rolf':      # all True
    print("Not all friends are named Rolf")
