"""
Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно следующим правилам:
все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед отсортированными четными
"""
s = input().strip()

# Разделяем символы на группы и сразу сортируем
lowercase = sorted([c for c in s if c.islower()])
uppercase = sorted([c for c in s if c.isupper()])
digits = sorted([c for c in s if c.isdigit()], key=lambda x: (int(x) % 2 == 0, x))

result = ''.join(lowercase + uppercase + digits)
print(result)


"Sorting1234"
# ginortS1324

"n0tEast3rEgg"
# aggnrsttEE30

"3DYrz34UXl"
# lrzDUXY334
