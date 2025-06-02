"""
Функция sourcetemplate()
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения.
Она начинается после вопросительного знака и идет до конца адреса.
Например:
https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
Реализуйте функцию sourcetemplate(), которая принимает один аргумент:
url — URL адрес
Функция sourcetemplate() должна возвращать функцию,
которая принимает произвольное количество именованных аргументов и возвращает url адрес,
объединенный со строкой запроса, сформированной из переданных аргументов.
При вызове без аргументов она должна возвращать исходный url адрес без изменений.
"""


def sourcetemplate(url):
    def query_string(**kwargs):
        nonlocal url
        res = []
        for k, v in sorted(kwargs.items()):
            res.append(f"{k}={v}")
        if res:
            url += "?" + "&".join(res)
        return url

    return query_string


url = "https://beegeek.ru"
load = sourcetemplate(url)
print(load(name="timur"))
# https://beegeek.ru?name=timur

url = "https://stepik.org/lesson/651459/step/14"
load = sourcetemplate(url)
print(load(thread="solutions", unit=648165))
# https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165

url = "https://all_for_comfort_life.com"
load = sourcetemplate(url)
print(load(smartphone="iPhone", notebook="huawei", sale=True))
# https://all_for_comfort_life.com?notebook=huawei&sale=True&smartphone=iPhone
