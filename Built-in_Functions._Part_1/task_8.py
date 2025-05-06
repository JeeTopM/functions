"""
Функция my_pow()
Реализуйте функцию my_pow(), которая принимает один аргумент:
number — целое неотрицательное число
Функция должна возвращать сумму, состоящую из цифр числа, возведенных в степень их порядкового номера.
"""


def my_pow(number):
    return sum(pow(int(i), n) for n, i in enumerate(str(number), 1))


print(my_pow(139))  # 739
print(my_pow(123))  # 32
print(my_pow(0))  # 0
