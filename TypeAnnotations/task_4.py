"""
Функция matrix_to_dict()
Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая принимает один аргумент:
matrix — матрица произвольной размерности, элементами которой являются целые или вещественные числа
Функция должна возвращать словарь, ключом в котором является номер строки матрицы, а значением — список элементов этой строки.
"""


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {num: elems for num, elems in enumerate(matrix, 1)}


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))
# {1: [5, 6, 7], 2: [8, 3, 2], 3: [4, 9, 8]}

matrix = [[5.1, 6, 7.94]]
print(matrix_to_dict(matrix))
# {1: [5.1, 6, 7.94]}

annotations = matrix_to_dict.__annotations__
print(annotations["return"])
# dict[int, list[int | float]]
