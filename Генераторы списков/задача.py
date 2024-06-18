# флоу решение:
# - генерируем числа от 0 до 100
# - фильтруем числа только те, которые делятся на 3 или на 5
# - собираем отфильтрованные числа в список

number = [x for x in range(1, 101) if x % 5 == 0 or x % 3 == 0]
# number_filter = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, number))
list_number = number
print(list_number)



