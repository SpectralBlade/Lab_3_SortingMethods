def parse_array(user_input: str) -> list[str | int | float]:
    """
    Функция для чтения введенного пользователем массива (для сортировок).
    :param user_input: введенный массив (в виде строки, значения через пробел)
    :return: список со значениями или ValueError
    """
    parts = user_input.split()
    try:
        return [int(x) for x in parts]
    except ValueError:
        pass

    try:
        return [float(x) for x in parts]
    except ValueError:
        pass

    if all(x.isalpha() for x in parts):
        return parts

    raise ValueError("ValueError: массив содержит разные типы данных")
