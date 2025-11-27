import unittest

from triangle import *


class TriangleAreaTestCase(unittest.TestCase):
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
        self.assertEqual(res, 50)

    def test_area_triangle(self):
        res = area(5, 10)
        self.assertEqual(res, 25)

    def test_area_triangle_float(self):
        res = area(5.123456, 5.123456)
        self.assertEqual(res, 13.12490069)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_perimeter_zero_a(self):
        res = perimeter(10, 0, 10)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_zero_b(self):
        res = perimeter(0, 5, 20)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_zero_c(self):
        res = perimeter(7, 5, 0)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter_negative_a(self):
        res = perimeter(-5, 10, 10)
        self.assertEqual(res, "Incorrect args")

    def test_perimeter(self):
        res = perimeter(10, 10, 20)
        self.assertEqual(res, 40)

    def test_perimeter_triangle_float(self):
        res = perimeter(5.12, 5, 5)
        self.assertEqual(res, 15.12)

    def test_perimeter_triangle_float_2(self):
        res = perimeter(5.123456, 5.123456, 5.123456)
        self.assertEqual(res, 15.370368)