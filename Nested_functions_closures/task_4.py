"""
Функция date_formatter()
Нередко в разных странах используются разные форматы дат.
Реализуйте функцию date_formatter(), которая принимает один аргумент:
country_code — код страны
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date)
и возвращает строку с данной датой в формате страны с кодом country_code.
"""

from datetime import date


def date_formatter(country_code):
    def ru(dt):
        return date.strftime(today, "%d.%m.%Y")  # DD.MM.YYYY

    def us(dt):
        return date.strftime(today, "%m-%d-%Y")  # MM-DD-YYYY

    def ca(dt):
        return date.strftime(today, "%Y-%m-%d")  # YYYY-MM-DD

    def br(dt):
        return date.strftime(today, "%d/%m/%Y")  # DD/MM/YYYY

    def fr(dt):
        return date.strftime(today, "%d.%m.%Y")  # DD.MM.YYYY

    def pt(dt):
        return date.strftime(today, "%d-%m-%Y")  # DD-MM-YYYY

    if country_code == "ru":
        return ru
    if country_code == "us":
        return us
    if country_code == "ca":
        return ca
    if country_code == "br":
        return br
    if country_code == "fr":
        return fr
    if country_code == "pt":
        return pt


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
