"""
Декоратор strip_range
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:
start — неотрицательное целое число
end — неотрицательное целое число
char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции,
заменяя все символы в диапазоне индексов от start (включительно) до end (не включительно) на символ char.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

import functools


def strip_range(start: int, end: int, char: str = "."):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:
            value = func(*args, **kwargs)
            chars = list(value)
            for i in range(start, min(end, len(chars))):
                chars[i] = char
            return "".join(chars)

        return wrapper

    return decorator


# 1
@strip_range(3, 5)
def beegeek():
    return "beegeek"


print(beegeek())
# bee..ek


# 2
@strip_range(3, 20, "_")
def beegeek():
    return "beegeek"


print(beegeek())
# bee____


# 3
@strip_range(20, 30)
def beegeek():
    return "beegeek"


print(beegeek())
# beegeek
