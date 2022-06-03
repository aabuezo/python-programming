x = 300
y = 300

print(id(x))
print(id(y))
print(x is y)


# slots
class Point(object):
    __slots__ = ('x', 'y')  # Point can only have these attributes


point = Point()
point.x = 5
point.y = 7
# point.name = 'Fred'     # ups... error


import sys


size_dict = sys.getsizeof(dict())
size_tuple = sys.getsizeof(tuple())
print(f'sizeof dict: {size_dict}')
print(f'sizeof tuple: {size_tuple}')


# GIL - Global Interpreter Lock
