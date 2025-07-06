"""
Декоратор trace
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения, а именно:
имя функции, переданные аргументы и возвращаемое значение в следующем формате:
TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""


import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'TRACE: вызов {func.__name__}() с аргументами: {tuple(args)}, {dict(kwargs)}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(result)}')
        return func(*args, **kwargs)
    print()
    return wrapper


# 1
@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')
'''
TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
TRACE: возвращаемое значение say(): 'Jane: Hello, World'
'''

# 2
@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c

print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)
'''
sub
прекрасная функция
TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
TRACE: возвращаемое значение sub(): 25
'''