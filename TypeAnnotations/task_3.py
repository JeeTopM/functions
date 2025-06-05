"""
Функция cyclic_shift()
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:
numbers — список целых или вещественных чисел
step — целое число
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None.
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
"""


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    shift = step % len(numbers)
    numbers[:] = numbers[-shift:] + numbers[:-shift]


"""
    s = step % len(numbers)
    if step < 0:
        left = numbers[:-s]
        right = numbers[-s:]
        numbers[:] = right + left
    else:
        left = numbers[-s:]
        right = numbers[:-s]
        numbers[:] = left + right

"""
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)
# [5, 1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)
# [3, 4, 5, 1, 2]
