import math


def area(r):
    if r < 0: return 'Incorrect radius'
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

