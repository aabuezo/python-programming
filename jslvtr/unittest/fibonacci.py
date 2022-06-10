from functools import cache


# @cache
def fibonacci(n: int) -> int:
    """
    funcion fibonacci para probar usando unittest
    :param n: numero entero positivo
    :return: el valor correspondiente a la serie de fibonacci para n
    fib(n) = fib(n - 1) + fib(n - 2)
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597...
    """
    if n < 0:
        # raise ValueError('fibonacci(n): n no puede ser negativo.')
        raise ValueError('fibonacci(n): n no puede ser negativo.')
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)