import time


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    return end - start


def powers(limit):
    return [x**2 for x in range(limit)]


# print(powers(5))
# number of seconds since 01-01-1970
start = time.time()
powers(5000000)
end = time.time()
print(end - start)


print(measure_runtime(lambda: powers(5000000)))


# timeit
import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
