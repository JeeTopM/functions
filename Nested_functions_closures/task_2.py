"""
Функция generator_square_polynom()
Рассмотрим семейство функций — квадратных трехчленов. Все эти функции имеют один и тот же вид:
f(x)=ax2+bx+c
Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:
a — вещественное число, коэффициент a
b — вещественное число, коэффициент b
c — вещественное число, коэффициент c
Функция generator_square_polynom() должна возвращать функцию,
которая принимает в качестве аргумента вещественное число x и возвращает значение выражения ax2+bx+c.
"""


def generator_square_polynom(a, b, c):
    pass


f = generator_square_polynom(1, 2, 1)
print(f(5))  # 36

print(generator_square_polynom(9, 52, 64)(8))  # 1056

ff = generator_square_polynom(26, 83, 22)
print(ff(55))  # 83237
