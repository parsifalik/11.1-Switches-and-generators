# Напишите генератор, генератор принимает на вход два списка и генерирует элементы, которые есть в обоих списках.
import random


# Определение функции-генератора intersection_generator
def intersection_generator(list_1, list_2):
    """
    Генератор, возвращает элементы, которые присутствуют в обоих списках lst_1 и lst_2.

    Args:
    - lst_1 (list): Первый список случайных чисел от 1 до 100.
    - lst_2 (list): Второй список случайных чисел от 1 до 100.

    Yield:
    - int: Элементы, которые присутствуют в обоих списках.
    """
    for item in list_1:
        if item in list_2:
            yield item


# Генерируем два списка случайных чисел от 1 до 100
lst_1 = [random.randint(1, 100) for _ in range(100)]
lst_2 = [random.randint(1, 100) for _ in range(100)]
# Создаем объект генератора
inter_gen = intersection_generator(lst_1, lst_2)

try:
    # Бесконечный цикл для итерации по генератору
    while True:
        # Выводим следующий элемент из генератора
        print(next(inter_gen))
        print(type(inter_gen))
except StopIteration:
    # Если достигнут конец генератора, выводим сообщение
    print("Конец итерации")
finally:
    # Блок finally выполняется всегда, вне зависимости от того, было ли исключение
    print("Завершение")
