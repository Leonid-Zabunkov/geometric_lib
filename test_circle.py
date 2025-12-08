import unittest

from circle import area

class CircleTestCase(unittest.TestCase):
   def test_zero_radius(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_negative_radius(self):
       res = area(-10)
       self.assertEqual(res, 'Incorrect radius')
       
   def test_valid_radius(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)
       
   def test_float_radius(self):
       res = area(1.2345)
       self.assertEqual(res, 4.787756573542472)
