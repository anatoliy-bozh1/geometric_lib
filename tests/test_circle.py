import unittest, math
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_basic(self):
        self.assertAlmostEqual(area(3), math.pi * 9, places=7)

    def test_perimeter_basic(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3, places=7)

    def test_zero(self):
        self.assertEqual(area(0), 0.0)
        self.assertEqual(perimeter(0), 0.0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-2)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            area("abc")
        with self.assertRaises(TypeError):
            perimeter("abc")

