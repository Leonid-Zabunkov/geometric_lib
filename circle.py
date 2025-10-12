import math


def area(r):
    """
    Рассчитывает площадь круга.

    Args:
        r: радиус круга

    Returns:
        Значение площади
    """
    return math.pi * r * r


def perimeter(r):
    """
    Рассчитывает периметр круга.

    Args:
        r: радиус круга

    Returns:
        Значение периметра
    """
    return 2 * math.pi * r

