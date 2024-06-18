Функция chain()
Функция chain() — объединяет несколько последовательностей в одну.

Чтобы работать с функцией chain, ее необходимо импортировать из модуля itertools:

from itertools import chain
chained_result = chain(iterable1, iterable2, ...)
iterable1, iterable2, ... — последовательности, которые нужно объединить.
Пример использования функции chain():

    # Объединить два списка в один
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined_list = list(chain(list1, list2))