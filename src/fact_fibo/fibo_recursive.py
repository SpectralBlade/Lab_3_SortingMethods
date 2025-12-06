def fibonacci_recursive(n: int, memory: dict = None) -> int:
    """
    :param n: вычисляется n-ое число Фибоначчи
    :param memory: словарь для сохранения уже посчитанных значений функции
    :return: результат
    """
    if memory is None:
        memory = {}

    if n < 0:
        raise ValueError("Подаваемое на вход число должно быть неотрицательным.")

    if n in memory:
        return memory[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_recursive(n - 1, memory) + fibonacci_recursive(n - 2, memory)

    memory[n] = result
    return result
