def factorial(n: int) -> int:
    """
    :param n: число, от которого нужно вычислить факториал
    :return: результат
    """
    if n < 0:
        raise ValueError('Подаваемое на вход число должно быть неотрицательным.')

    if n == 1:
        return 1
    elif n == 0:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result