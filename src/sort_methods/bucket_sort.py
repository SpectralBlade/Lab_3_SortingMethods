from Lab_3_SortingMethods.src.sort_methods.quick_sort import quick_sort

def bucket_sort(array: list[float],
                buckets: int | None = None) -> list[float]:
    """
    Функция для сортировки ведрами (сравнение 2 чисел поочередно).
    :param array: Массив для сортировки
    :param buckets: Желаемое количество ведер
    :return: Отсортированный список
    """
    if array is None:
        return []

    if any(x < 0 or x >= 1 for x in array):
        raise ValueError("Bucket sort ожидает числа в диапазоне [0, 1)")

    if buckets is None:
        buckets = len(array)

    bucket_list = [[] for _ in range(buckets)]

    for num in array:
        bucket_num = int(num * buckets)
        if bucket_num == buckets:
            bucket_num = buckets - 1
        bucket_list[bucket_num].append(num)

    for i, bucket in enumerate(bucket_list):
        if len(bucket) > 1:
            sorted_bucket = quick_sort(bucket)
            bucket_list[i] = sorted_bucket

    result = []
    for bucket in bucket_list:
        result.extend(bucket)

    return result
