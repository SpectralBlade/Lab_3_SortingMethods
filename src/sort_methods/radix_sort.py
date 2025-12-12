from Lab_3_SortingMethods.src.sort_methods.counting_sort import counting_sort_for_radix

def radix_sort(array: list[int], base: int = 10) -> list[int]:
    """
    Функция для подразрядной сортировки.
    :param array: Массив для сортировки
    :param base: Основание системы счисления (по умолчанию 10)
    :return: Отсортированный список
    """
    if not array:
        return []

    if any((not isinstance(x, int)) or x < 0 for x in array):
        raise ValueError('ValueError: Radix sort поддерживает только натуральные числа + 0')

    arr = array.copy()

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp, base)
        exp *= base

    return arr