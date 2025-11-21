import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_basic(self):
        self.assertEqual(area(6, 4), 12)

    def test_perimeter_basic(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_zero(self):
        self.assertEqual(area(6, 0), 0)
        self.assertEqual(perimeter(0, 4, 5), 9)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-1, 2)
        with self.assertRaises(ValueError):
            area(2, -1)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            area("abc", 4)
        with self.assertRaises(TypeError):
            perimeter(3, "abc", 5)

