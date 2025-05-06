"""
Функция non_negative_even()
Реализуйте функцию non_negative_even(),  которая принимает один аргумент:
numbers — непустой список чисел
Функция должна возвращать True, если все числа в списке numbers являются четными и неотрицательными, или False в противном случае.
"""


def non_negative_even(numbers):
    return all(i >= 0 and i % 2 == 0 for i in numbers)


print(non_negative_even([0, 2, 4, 8, 16]))
# True
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
# False
print(non_negative_even([0, 0, 0, 0, 0]))
# True
