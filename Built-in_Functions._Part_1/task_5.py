"""
Функция is_greater()
Реализуйте функцию is_greater(), которая принимает два аргумента в следующем порядке:
lists — список, элементами которого являются списки целых чисел
number — целое число
Функция должна возвращать True, если хотя бы в одном вложенном списке из списка lists
    сумма всех элементов больше number, или False в противном случае.
"""


def is_greater(lists, number):
    return any(sum(i) > number for i in lists)


data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))
# True
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))
# False
data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
print(is_greater(data, 3))
# False
