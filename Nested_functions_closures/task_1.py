"""
Функция power()
Реализуйте функцию power(), которая принимает один аргумент:
degree — целое число
Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x
и возвращает значение x в степени degree.
"""


def power(degree):
    def func(x):
        return pow(x, degree)
    return func

square = power(2)
print(square(5))  # 25

print(power(3)(3)) # 27

result = power(4)(2)
print(result)  # 16