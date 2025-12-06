from functools import cmp_to_key
from typing import Callable, Any

def quick_sort(array: list, key: Callable[[Any], Any] = None,
               cmp: Callable[[Any, Any], int] = None):
    """
    Функция для быстрой сортировки относительно pivot.
    :param array: Массив для сортировки
    :param key: Ключ (из заданного списка)
    :param cmp: Компаратор (из заданного списка)
    :return: Отсортированный список
    """
    if cmp is not None:
        key = cmp_to_key(cmp)

    if key is None:
        key = lambda x: x

    arr = array.copy()
    if len(arr) < 2:
        return arr

    pivot = arr[-1]
    pivot_key = key(pivot)

    left = [x for x in arr if key(x) < pivot_key]
    middle = [x for x in arr if key(x) == pivot_key]
    right = [x for x in arr if key(x) > pivot_key]

    return quick_sort(left, key, None) + middle + quick_sort(right, key, None)
