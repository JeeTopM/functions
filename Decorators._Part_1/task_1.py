"""
Декоратор sandwich
Реализуйте декоратор sandwich, который выводит тексты:
---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
до и после вызова декорируемой функции соответственно.
"""


def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        res = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return res

    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(" | ".join(ingredients))


add_ingredients(["томат", "салат", "сыр", "бекон"])
"""
---- Верхний ломтик хлеба ----
томат | салат | сыр | бекон
---- Нижний ломтик хлеба ----
"""
print()


@sandwich
def beegeek():
    return "beegeek"


print(beegeek())
"""
---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
beegeek
"""
