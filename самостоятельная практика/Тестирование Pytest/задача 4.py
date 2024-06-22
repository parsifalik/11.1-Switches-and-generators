# Найдите среднее арифметическое всех чисел, кратных 3 или 5, в заданном диапазоне.

number = range(21)
filter_numbers = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, number))
average = sum(filter_numbers) / len(filter_numbers)
print(average)

