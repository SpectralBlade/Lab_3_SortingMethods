def factorial_recursive(n: int, memory: dict = None) -> int:
    """
    Функция для вычисления факториала рекурсивно.
    :param n: число, от которого нужно вычислить факториал
    :param memory: словарь для сохранения уже посчитанных значений функции
    :return: результат
    """
    if memory is None:
        memory = {}

    if n == 0 or n == 1:
        return 1

    if n < 0:
        raise ValueError('Подаваемое на вход число должно быть неотрицательным.')

    if n in memory:
        return memory[n]

    result = n*factorial_recursive(n-1, memory)
    memory[n] = result
    return result
