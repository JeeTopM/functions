"""
Декоратор repeat
Реализуйте декоратор repeat, который принимает один аргумент:
times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


# 1
@repeat(3)
def say_beegeek():
    """documentation"""
    print("beegeek")


say_beegeek()
"""
beegeek
beegeek
beegeek
"""


# 2
@repeat(4)
def say_beegeek():
    """documentation"""
    print("beegeek")


print(say_beegeek.__name__)
print(say_beegeek.__doc__)
"""
say_beegeek
documentation
"""


# 3
@repeat(10)
def add(a, b):
    """sum of two numbers"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))
