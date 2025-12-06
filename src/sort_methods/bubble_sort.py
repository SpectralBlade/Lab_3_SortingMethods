from functools import cmp_to_key
from typing import Callable, Any

def bubble_sort(array: list, key: Callable[[Any], Any] = None,
                cmp: Callable[[Any, Any], int] = None) -> list:
    """
    Функция для сортировки пузырьком (сравнение 2 чисел поочередно).
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
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr
