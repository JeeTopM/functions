"""
Функция custom_isinstance()
Реализуйте функцию custom_isinstance(), которая принимает два аргумента в следующем порядке:
objects — список произвольных объектов
typeinfo — тип данных или кортеж с типами
Функция должна возвращать единственное число — количество объектов из списка objects,
    которые принадлежат типу typeinfo или одному из типов, если был передан кортеж.
"""


def custom_isinstance(objects, typeinfo):
    return sum(isinstance(i, typeinfo) for i in objects)


"""    cht = 0
    for i in objects:
        cht += isinstance(i, typeinfo)
    return cht"""

numbers = [1, "two", 3.0, "четыре", 5, 6.0]
print(custom_isinstance(numbers, int))

# 2
numbers = [1, "two", 3.0, "четыре", 5, 6.0]
print(custom_isinstance(numbers, (int, float)))

# 4
numbers = [1, "two", 3.0, "четыре", 5, 6.0]
print(custom_isinstance(numbers, list))
# 0
