"""
Новый print()
Напишите программу, которая переопределяет встроенную функцию print() так,
чтобы она печатала все переданные строковые аргументы в верхнем регистре.
"""

old_print = print


def print(*args, sep=" ", end="\n"):
    caps = (c.upper() if isinstance(c, str) else c for c in args)
    old_print(*caps, sep=sep.upper(), end=end.upper())


print("beegeek", [1, 2, 3], 4)  # BEEGEEK [1, 2, 3] 4
print("bee", "geek", sep=" and ", end=" wow")  # BEE AND GEEK WOW

words = ("black", "white", "grey", "black-1", "white-1", "python")
print(*words, sep=" to ", end=" LOVE")
