# Создаем список случайных значений
random_values = [random.randint(0, 9) for _ in range(5)]
========================================================
# Генератор списков использует квадратные скобки
[x * x for x in range(10)]

>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Генераторное выражение использует круглые скобки
(x * x for x in range(10))

>>> <generator object <genexpr> at 0x7fe76f7e5db0>
=================================================
print(*(x for x in "Hello World!" if x.isupper()))

>>> H W

Давайте разберем пример пошагово:
1) Генераторное выражение:

    (x for x in "Hello World!" if x.isupper())
    Здесь создается генераторное выражение, которое фильтрует символы строки "Hello World!", оставляя только заглавные буквы. if x.isupper() — это условие, проверяющее, является ли символ заглавной буквой.

2) Печать с использованием print(*...):

    print(*(x for x in "Hello World!" if x.isupper()))
    С помощью print(*...) мы передаем каждую заглавную букву в функцию print() как отдельный аргумент. Звездочка * перед генераторным выражением распаковывает его элементы.

3) Результат выполнения:

    H W
    В результате выполнения этого кода функция print() выводит заглавные буквы из строки "Hello World!" разделяя их пробелом — H W
==================================================================================================================================
result = [x for num in range(20) for x in [num, num] if num % 2 == 0]
# [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, ..., 18, 18]
=====================================================
Квадраты чисел

squares = [x*x for x in [1, 2, 3]]

    [1, 4, 9]

    x*x — выражение, которое вычисляется для каждого элемента x.

    for x in [1, 2, 3] — цикл, который проходит по значениям в списке [1, 2, 3]
===============================================================================
ascii_codes = [ord(c) for c in "Hello!!" if c.isalpha() and c.islower()]

    [101, 108, 108, 111]

    ord(c) — выражение, вычисляющее ASCII-код для каждого символа c
===================================================================
matching_indices = [i for i, (x, y) in enumerate([(1, 2), (4, 4), (5, 7), (0, 0)]) if x == y]

    [1, 3]

    i — переменная, представляющая индекс элемента.
    (x, y) — кортеж, представляющий пару значений.
    enumerate([(1, 2), (4, 4), (5, 7), (0, 0)]) — функция, возвращающая индекс и элементы перечисления.
    if x == y — условие, фильтрующее пары с одинаковыми элементами.
======================================================================================================

алгоритм написания
Списковое включение (list comprehension):
[expression for item in iterable if condition]

squares = [x ** 2 for x in range(10) if x % 2 == 0]
# squares будет содержать [0, 4, 16, 36, 64]
============================================
Включение множества (set comprehension):
{expression for item in iterable if condition}

unique_squares = {x ** 2 for x in range(10) if x % 2 == 0}
# unique_squares будет содержать {0, 4, 16, 36, 64}
===================================================
Включение словаря (dict comprehension):
{key_expression: value_expression for item in iterable if condition}
square_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
# square_dict будет содержать {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
===============================================================
Генераторное выражение (generator expression):
(expression for item in iterable if condition)
squares_gen = (x ** 2 for x in range(10) if x % 2 == 0)
# squares_gen будет генератором, который генерирует 0, 4, 16, 36, 64
====================================================================
Примеры синтаксиса с условием:
Списковое включение с условием
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# even_squares будет содержать [0, 4, 16, 36, 64]
Генераторное выражение с условием
even_squares_gen = (x ** 2 for x in range(10) if x % 2 == 0)
# even_squares_gen будет генератором, который генерирует 0, 4, 16, 36, 64

