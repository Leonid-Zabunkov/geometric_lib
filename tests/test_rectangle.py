import unittest

from rectangle import *


class RectangleAreaTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(10, 0)
        self.assertEqual(res, "Incorrect args")

    def test_area_zero_b(self):
        res = area(0, 5)
        self.assertEqual(res, "Incorrect args")

    def test_area_negative_a(self):
        res = area(-5, 10)
        self.assertEqual(res, "Incorrect args")

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_rectangle(self):
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_area_rectangle_float(self):
        res = area(5.123456, 5.123456)
        self.assertEqual(res, 26.24980138)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_perimeter_zero_a(self):
        res = perimeter(10, 0)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_zero_b(self):
        res = perimeter(0, 5)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_negative_a(self):
        res = perimeter(-5, 10)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_rectangle(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_perimeter_rectangle_float(self):
        res = perimeter(5.12, 5)
        self.assertEqual(res, 20.24)

    def test_perimeter_rectangle_float_2(self):
        res = perimeter(5.123456, 5.123456)
        self.assertEqual(res, 20.493824)
