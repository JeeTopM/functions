"""
Математические выражения
Напишите программу, которая принимает на вход произвольное количество строк,
содержащих корректные математические выражения, и выводит значение наибольшего из них.
"""

import sys

examples = [e.strip() for e in sys.stdin]
print(max(eval(e) for e in examples))

# print(max(map(eval, sys.stdin)))
"""
1 + 2 + 3
2 * 8
10 * 10 - 1
"""
# 99
