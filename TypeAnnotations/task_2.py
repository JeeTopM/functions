"""
Функция top_grade()
Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:
grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по ключу grades
Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.
"""


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {"name": grades["name"], "top_grade": max(grades["grades"])}


info = {"name": "Timur", "grades": [30, 57, 99]}
print(top_grade(info))
# {'name': 'Timur', 'top_grade': 99}

print(top_grade({"name": "Ruslan", "grades": [19, 48, 86, 45, 32]}))
# {'name': 'Ruslan', 'top_grade': 86}


annotations = top_grade.__annotations__
print(annotations["grades"])
# dict[str, str | list[int]]

print(*top_grade.__annotations__.values())
