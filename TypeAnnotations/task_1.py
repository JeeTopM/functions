"""
Функция get_digits()
Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает один аргумент:
number — положительное целое или вещественное число
Функция должна возвращать список, состоящий из цифр числа number.
"""


def get_digits(number: int | float) -> list[int]:
    return [int(i) for i in str(number) if i.isdigit()]


print(get_digits(16733))
# [1, 6, 7, 3, 3]

print(get_digits(13.909934))
# [1, 3, 9, 0, 9, 9, 3, 4]

annotations = get_digits.__annotations__
print(annotations["return"])
# list[int]

annotations = get_digits.__annotations__
print(annotations["number"])
