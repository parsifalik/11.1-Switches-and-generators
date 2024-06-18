"Дан список словарей. Отфильтруйте его по ключу age и значению 30."""

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

filter_people = list(filter(lambda x: x['age'] == 30, people))
print(filter_people)

name = list(name for name in people if name['age'] == 30)
print(name)

