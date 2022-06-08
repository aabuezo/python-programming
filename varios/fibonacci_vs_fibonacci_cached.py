import time
from functools import cache, lru_cache

NUM1 = 40
NUM2 = 400  # NO es 10 veces mas que NUM1 !!!
# fibonacci es O(2^n) por lo que:
# NUM1 es 2^40
# NUM2 es 2^400


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print(fibonacci(NUM1))
end = time.time()
print(f'fibonacci: {end - start} seg.')


# con @cache, fibonacci es lineal O(n)...
# @cache
@lru_cache(maxsize=10)
def cached_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


start = time.time()
print(cached_fibonacci(NUM2))
end = time.time()
print(f'cached fibonacci: {end - start} seg.')
