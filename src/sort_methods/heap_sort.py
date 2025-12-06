from functools import cmp_to_key
from typing import Callable, Any

def heap_sort(array: list,
              key: Callable[[Any], Any] = None,
              cmp: Callable[[Any, Any], int] = None) -> list:
    """
    Функция для сортировки кучей (на двоичной куче).
    :param array: Массив для сортировки
    :param key: Ключ (из заданного списка)
    :param cmp: Компаратор (из заданного списка)
    :return: Отсортированный список
    """

    if cmp is not None:
        key = cmp_to_key(cmp)

    if key is None:
        key = lambda x: x

    arr = [(key(x), i, x) for i, x in enumerate(array)]
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return [x[2] for x in arr]


def heapify(arr, n, i):
    """
    Вспомогательная функция для сортировки кучей.
    Приводит поддерево с корнем в индексе i к свойству двоичной кучи.
    :param arr: Список элементов-кортежей, представляющих бинарную кучу
    :param n: Текущее число элементов в куче
    :param i: Индекс вершины, для которой необходимо восстановить свойство кучи
    :return: Данная функция ничего не возвращает
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
