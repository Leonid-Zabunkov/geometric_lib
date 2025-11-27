def area(a):
    """
    Рассчитывает площадь квадрата.

    Args:
        a: Сторона квадрата

    Returns:
        Значение площади
    """
    if a <= 0:
        return "Incorrect args"
    return round(a * a, 8)


def perimeter(a):
    """
    Рассчитывает периметр квадрата.

    Args:
        a: Сторона квадрата

    Returns:
        Значение периметра
    """
    if a <= 0:
        return "Incorrect args"
    return round(4 * a, 8)
