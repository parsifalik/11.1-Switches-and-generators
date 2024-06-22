import pytest
from task_3 import intersection_generator


# дублирование чисел
def test_duplicate_list():
    lst_1 = [1, 2, 3, 4, 5]
    lst_2 = [3, 4, 5, 6, 7]
    expected = [3, 4, 5,]

    result = list(intersection_generator(lst_1, lst_2))
    assert result == expected


# пустой список
def test_none():
    list_1 = []
    list_2 = []
    expected = []
    result = list(intersection_generator(list_1, list_2))
    assert result == expected


@pytest.mark.parametrize(
    "list_1, list_2, expected",
    [
        (
            [1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [3, 4, 5]
        ),
        (
            [], [], []
        )
    ]
)
def test_duplicate_and_none_lists(list_1, list_2, expected):
    result = list(intersection_generator(list_1, list_2))
    assert result == expected
    assert result == expected


