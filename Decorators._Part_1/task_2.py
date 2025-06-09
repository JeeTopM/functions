"""
Новый print
Напишите программу с использованием декоратора, которая переопределяет функцию print() так,
чтобы она печатала весь текст в верхнем регистре.
"""

import builtins


def upper_case(func):
    def wrapper(*args, **kwargs):
        new_args = [arg.upper() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {
            key: value.upper() if isinstance(value, str) else value
            for key, value in kwargs.items()
        }
        return func(*new_args, **new_kwargs)

    return wrapper


print = upper_case(builtins.print)


print("hi", "there", end="!")
# HI THERE!
print("are you in trouble?")
# ARE YOU IN TROUBLE?
print(111, 222, 333, sep="xxx")
# 111XXX222XXX333
