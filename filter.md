Функция filter()

Функция filter() — фильтрует элементы из входной последовательности на основе заданного условия.

Синтаксис функции:

filter_result = filter(predicate, iterable)

    predicate — функция, возвращающая True или False для каждого элемента. Элементы, для которых возвращается True, сохраняются в новую последовательность.

Функции-предикаты (или просто предикаты) — это функции, которые возвращают булево значение True или False в зависимости от того, выполняется ли какое-то условие. Иными словами, они проверяют некоторое утверждение и возвращают ответ на вопрос: «Верно ли это утверждение?»

    iterable — последовательность, которую нужно отфильтровать.

Пример использования функции filter():

# Оставить только четные числа
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

В этом примере происходит фильтрация списка numbers для того, чтобы оставить в нем только четные числа, используя функцию filter() в сочетании с лямбда-функцией.

Давайте подробнее рассмотрим каждый шаг:

    Функция filter() принимает два аргумента: функцию и итерируемый объект. filter() применяет переданную в качестве аргумента функцию к каждому элементу итерируемого объекта и возвращает новый итератор с теми элементами, для которых функция вернула True

    Лямбда-функция lambda x: x % 2 == 0 проверяет, делится ли число x на 2 без остатка. Если x четное, то есть x % 2 равно 0, функция возвращает True

    Результатом работы функции filter() будет объект, который содержит только те элементы из списка numbers, которые удовлетворяют условию четности (деление на 2 без остатка). Например, из исходного списка 1, 2, 3, 4, 5 четными являются 2 и 4

Для преобразования результата в список можно использовать функцию list()

Пример:

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

После этого преобразования even_numbers будет содержать [2, 4], что представляет собой четные числа из исходного списка numbers