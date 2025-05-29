"""
Функция polynom()
Реализуйте функцию polynom(), которая принимает один аргумент:
x — целое число
Функция должна возвращать значение выражения x2+1.

Также функция должна иметь атрибут values, представляющий собой множество
    (тип set) всех значений функции, которые уже были вычислены.
"""


def polynom(x):
    res = pow(x, 2) + 1
    if not hasattr(polynom, 'values'):
        polynom.values = set()
    polynom.values.add(res)
    return res


print(polynom(5))
print(polynom.values)
"""
26
{26}
"""
