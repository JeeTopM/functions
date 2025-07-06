"""
Декоратор prefix
Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
string — произвольная строка
to_the_end — булево значение, по умолчанию равное False
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции.
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

import functools


def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if to_the_end:
                return result + string
            else:
                return string + result

        return wrapper

    return decorator


# 1
@prefix("€")
def get_bonus():
    return "2000"


print(get_bonus())
# €2000


# 2
@prefix("$$$", to_the_end=True)
def get_bonus():
    return "2000"


print(get_bonus())
# 2000$$$
