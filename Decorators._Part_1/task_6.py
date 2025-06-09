"""
Декоратор takes_positive
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.
Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
* TypeError, если аргумент не является целым числом
* ValueError, если аргумент является целым числом, но отрицательным или равным нулю
"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        if not all(isinstance(x, int) for x in all_args):
            return TypeError
        if not all(x > 0 for x in all_args):
            return ValueError
        else:
            return func(*args, **kwargs)

    return wrapper


"""
        if all(isinstance(x, int) for x in all_args) and all(x > 0 for x in all_args):
            return sum(all_args)
        elif all(isinstance(x, int) for x in all_args) and any(x > 0 for x in all_args):
            return ValueError
        elif any(isinstance(x, not int) for x in all_args):
            return TypeError
"""


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))  # <class 'ValueError'>


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum("10", 20, 10))
except Exception as err:
    print(type(err))  # <class 'TypeError'>
