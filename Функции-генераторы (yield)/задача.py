# написать генератор бесконечной последовательности чисел
# флоу решение:
# - определить функцию генератор
# - запустить бесконечный цикл
# - сгенерировать число
# - увеличить число на 1
# - получить значение из генератора

def inf_seq(num=1):
    while True:
        yield num
        num += 2


number = inf_seq()
print(next(number))
print(next(number))

#=====================================
from typing import List, Dict, Any, Generator

def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Generator[Dict[str, Any], None, None]:
    for transaction in transactions:
        if transaction.get('currency_code') == currency_code:
            yield transaction


transactions = [
    {'id': 1, 'currency_code': 'USD', 'amount': 100},
    {'id': 2, 'currency_code': 'EUR', 'amount': 200},
    {'id': 3, 'currency_code': 'USD', 'amount': 150},
]

filtered_transactions = filter_by_currency(transactions, 'USD')

# Используем генератор в цикле for
for transaction in filtered_transactions:
    print(transaction)


# {'id': 1, 'currency_code': 'USD', 'amount': 100}
# {'id': 3, 'currency_code': 'USD', 'amount': 150}

