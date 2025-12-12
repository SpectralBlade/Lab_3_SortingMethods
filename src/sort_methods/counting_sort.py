def counting_sort(array: list[int]) -> list[int]:
    """
    Функция для сортировки подсчетом (заведение n счетчиков для n = max(array) натуральных чисел.)
    :param array: Массив для сортировки
    :return: Отсортированный список
    """
    if not array:
        return []

    if any((not isinstance(x, int)) or x < 0 for x in array):
        raise ValueError("ValueError: Counting sort поддерживает только натуральные числа + 0")

    max_val = max(array)
    min_val = min(array)
    count_size = max_val - min_val + 1
    count = [0] * count_size

    for num in array:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [0] * len(array)

    for num in reversed(array):
        pos = count[num - min_val] - 1
        result[pos] = num
        count[num - min_val] -= 1

    return result


def counting_sort_for_radix(array: list[int], exp: int, base: int) -> list[int]:
    """
    Вспомогательная функция для поразрядной сортировки (radix sort).
    :param array: Массив для сортировки
    :param exp: Позиция разряда
    :param base: Основание системы счисления (по умолчанию 10).
    :return: Отсортированный список
    """
    n = len(array)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        digit = (array[i] // exp) % base
        count[digit] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (array[i] // exp) % base
        output[count[digit] - 1] = array[i]
        count[digit] -= 1

    return output