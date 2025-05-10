"""
Коллекции
Напишите программу, которая принимает на вход корректный непустой список,
    корректный непустой кортеж или корректное множество произвольной длины, и выполняет следующее:
если введен список, выводит его последний элемент
если введен кортеж, выводит его первый элемент
если введено множество, выводит количество его элементов
"""

def non_empty_list(data):
    if isinstance(data, list):
        return data[-1]
    elif isinstance(data, tuple):
        return data[0]
    elif isinstance(data, set):
        return len(data)
        

d = [[1, 2], [3, 4], [5, 6]]
# [5, 6]
d = {"Arthur", "Timur", "Anri", "Ruslan", "Dima"}
# 5
d = ("black", "blue", "red", "orange", "green", "gray")
# black

print(non_empty_list(eval(input())))