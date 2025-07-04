"""
Декоратор square
Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во вторую степень.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return wrapper


# 1
@square
def add(a, b):
    return a + b


print(add(3, 7))
"""
100
"""


# 2
@square
def add(a, b):
    """прекрасная функция"""
    return a + b


print(add(1, 1))
print(add.__name__)
print(add.__doc__)
"""
4
add
прекрасная функция
"""


# 3
@square
def beegeek():
    """beegeek docs"""
    return 99


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)
