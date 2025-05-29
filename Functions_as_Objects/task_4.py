"""
Функция remove_marks()
Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:
text — произвольная строка
marks — набор символов
Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.
"""


def remove_marks(text, marks):
    remove_marks.__dict__["count"] = remove_marks.__dict__.get("count", 0) + 1
    for i in marks:
        text = text.replace(i, "")
    return text


text = "Hi! Will we go together?"

print(remove_marks(text, "!?"))
print(remove_marks.count)