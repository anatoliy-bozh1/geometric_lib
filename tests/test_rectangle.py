import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(area(3, 5), 15)
        self.assertEqual(perimeter(3, 5), 16)

    def test_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(perimeter(10, 0), 20)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-1, 2)
        with self.assertRaises(ValueError):
            perimeter(2, -1)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            area("abc", 4)
        with self.assertRaises(TypeError):
            perimeter(3, "abc")

