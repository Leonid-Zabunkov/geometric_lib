import unittest

from square import *


class SquareAreaTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0)
        self.assertEqual(res, "Incorrect args")

    def test_area_negative_a(self):
        res = area(-5)
        self.assertEqual(res, "Incorrect args")

    def test_area_square(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_square_float(self):
        res = area(5.123456)
        self.assertEqual(res, 26.24980138)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_perimeter_zero_a(self):
        res = perimeter(0)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_negative_a(self):
        res = perimeter(-5)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_square(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_square_float(self):
        res = perimeter(5.12)
        self.assertEqual(res, 20.48)

    def test_perimeter_square_float_2(self):
        res = perimeter(5.123456)
        self.assertEqual(res, 20.493824)
