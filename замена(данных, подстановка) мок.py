import pytest
from unittest.mock import patch
from src.generators import card_number_generator
# Определение теста с использованием patch:
def test_card_number_generator_with_fixed_value():
    with patch('src.generators.random.randint', return_value=5):
        quantity = 5
        card_numbers = list(card_number_generator(quantity, 0, 9))
        expected_card_number = "5555 5555 5555 5555"
        for card in card_numbers:
            assert card == expected_card_number, f"Expected {expected_card_number}, got {card}"
# Запуск тестов:
if __name__ == "__main__":
    pytest.main()
# Объяснение кода теста
Объяснение кода теста

    Контекстный менеджер with patch('src.generators.random.randint', return_value=5):
        Здесь используется patch для замены функции random.randint, которая находится в модуле src.generators. Все вызовы random.randint внутри функции card_number_generator будут возвращать 5.

    Вызов card_number_generator:
        Генерируется 5 номеров карт с использованием card_number_generator. Поскольку все случайные цифры заменены на 5, каждый номер карты будет выглядеть как "5555 5555 5555 5555".

    Проверка результатов:
        Проверяется, что каждый сгенерированный номер карты соответствует ожидаемому значению.

Почему это работает?

Когда вы используете patch для замены random.randint, он заменяет функцию в указанном модуле (src.generators), а не глобально во всём проекте. 
Это позволяет контролировать поведение функции card_number_generator во время тестирования, не изменяя её код.

  Заключение

Использование patch позволяет замокать зависимости, такие как random.randint, даже если они находятся внутри тестируемой функции. 
Это обеспечивает предсказуемое поведение и позволяет вам тестировать функции, зависящие от случайных значений.
