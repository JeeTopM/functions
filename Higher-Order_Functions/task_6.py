"""
Реализуйте функцию verification(), которая проверяет правильность введенного пароля.
Она должна принимать четыре аргумента в следующем порядке:
    login — логин пользователя
    password — пароль пользователя
    success — некоторая функция
    failure — некоторая функция
Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна
строчная латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success() с аргументом login,
если переданный пароль является правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об ошибке:
    в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
    в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
    в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
    в пароле нет ни одной цифры, если в пароле отсутствуют цифры
"""

from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits


def success(login):
    print(f"Привет, {login}!")


def failure(login, text):
    print(f"{login}, попробуйте снова. Ошибка: {text}")


def verification(login, password, success, failure):
    d = {
        0: "в пароле нет ни одной буквы",
        1: "в пароле нет ни одной заглавной буквы",
        2: "в пароле нет ни одной строчной буквы",
        3: "в пароле нет ни одной цифры",
    }
    if not any(map(lambda x: x in ascii_letters, password)):
        failure(login, d[0])
    elif not any(map(lambda x: x in ascii_uppercase, password)):
        failure(login, d[1])
    elif not any(map(lambda x: x in ascii_lowercase, password)):
        failure(login, d[2])
    elif not any(map(lambda x: x in digits, password)):
        failure(login, d[3])
    else:
        success(login)


verification("timyrik20", "Beegeek314", success, failure)

# Привет, timyrik20!

verification("Ruslan_Chaniev", "stepikstepik2", success, failure)

# Ruslan_Chaniev, попробуйте снова. Текст ошибки: в пароле нет ни одной заглавной буквы
