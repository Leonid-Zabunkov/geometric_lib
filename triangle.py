def area(a, h):
    """
    Рассчитывает площадь треугольника.

    Args:
        a: Длина основания
        h: Высота, проведённая к основанию

    Returns:
        Значение площади
    """
    if a <= 0 or h <= 0:
        return "Incorrect args"

    return round(a * h / 2, 8)


def perimeter(a, b, c):
    """
    Рассчитывает периметр треугольника.

    Args:
        a: длина первой стороны
        b: длина второй стороны
        c: длина третей стороны

    Returns:
        Значение периметра
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Incorrect args"

    return round(a + b + c, 8)
