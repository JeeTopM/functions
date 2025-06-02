"""
Функция date_formatter()
Нередко в разных странах используются разные форматы дат.
Реализуйте функцию date_formatter(), которая принимает один аргумент:
country_code — код страны
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date)
и возвращает строку с данной датой в формате страны с кодом country_code.
"""

from datetime import date


def date_formatter():
    pass


date_ru = date_formatter("ru")
today = date(2022, 1, 25)
print(date_ru(today))
# 25.01.2022

date_ru = date_formatter("us")
today = date(2025, 1, 5)
print(date_ru(today))
# 01-05-2025

date_ru = date_formatter("ca")
today = date(2015, 12, 7)
print(date_ru(today))
# 2015-12-07
