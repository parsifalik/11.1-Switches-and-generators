from itertools import chain
# Объедините несколько списков в один список, учитывая возможные дубликаты элементов.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]

word = list(set(chain(list1, list2, list3)))
print(word)