"""
Декоратор do_twice
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.
"""


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def beegeek():
    print("beegeek")


beegeek()
# beegeek
# beegeek
print("---")


@do_twice
def beegeek():
    print("beegeek")


print(beegeek())

# beegeek
# beegeek
# None
