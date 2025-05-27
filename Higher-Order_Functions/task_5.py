"""
Реализуйте функцию print_operation_table(), которая принимает три аргумента в следующем порядке:
operation — функция, характеризующая некоторую бинарную операцию
rows — натуральное число
cols — натуральное число
Функция должна составлять и выводить таблицу из rows строк и cols столбцов,
в которой элемент со строкой n и столбцом m имеет значение operation(n, m).
"""


def print_operation_table(operation, rows, cols):
    for r in range(1, rows+1):
        # print(*map(operation, [i] * cols, range(1, cols + 1)))
        res = []
        for c in range(1, cols+1):
            res.append(f'{operation(r,c):3}')
        print(*res)

print_operation_table(lambda a, b: a * b, 5, 5)
"""
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
"""
print_operation_table(pow, 5, 4)
"""
1   1   1   1
2   4   8   16
3   9   27  81
4   16  64  256
5   25  125 625
"""
