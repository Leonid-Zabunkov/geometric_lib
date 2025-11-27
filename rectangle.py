def area(a, b):
    """
    Рассчитывает площадь прямоугольника.

    Args:
        a: длина первой стороны
        b: длина второй стороны

    Returns:
        Значение площади
    """
    if a <= 0 or b <= 0:
        return "Incorrect args"
    return round(a * b, 8)


def perimeter(a, b):
    """
    Рассчитывает периметр прямоугольника.

    Args:
        a: длина первой стороны
        b: длина второй стороны

    Returns:
        Значение периметра
    """
    if a <= 0 or b <= 0:
        return "Incorrect args"
    return round((a + b) * 2, 8)

