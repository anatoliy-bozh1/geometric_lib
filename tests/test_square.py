import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(perimeter(4), 16)

    def test_zero(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            area("abc")
        with self.assertRaises(TypeError):
            perimeter("abc")

