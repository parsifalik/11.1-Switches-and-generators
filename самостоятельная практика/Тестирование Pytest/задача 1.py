# Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10.
cube_number = list(x * x for x in range(11) if x % 2 == 0)
print(cube_number)
