def fibonacci(n: int) -> int:
    """
    :param n: вычисляется n-ое число Фибоначчи
    :return: результат
    """
    if n < 0:
        raise ValueError("Подаваемое на вход число должно быть неотрицательным.")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b