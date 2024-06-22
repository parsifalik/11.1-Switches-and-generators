# Напишите генератор, который генерирует случайные числа в заданном диапазоне.
# Для решения задачи вы можете использовать random.randint(a, b). random.randint(a, b) — это функция в модуле random
# которая генерирует случайное целое число в диапазоне от a до b включительно. Оба аргумента должны быть целыми числами.
# Если a больше, чем b, то randint автоматически поменяет их местами, чтобы a было меньше или равно b
import random


def random_number(start, stop):
    while True:
        yield random.randint(start, stop)


ran_num = random_number(1, 20)

for num in range(10):
    print(next(ran_num))

