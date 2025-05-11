import unittest
from triangle import is_triangle

class TestTriangleChecker(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(is_triangle(3, 4, 5))

    def test_invalid_triangle(self):
        self.assertFalse(is_triangle(1, 2, 3))  # 1+2 = 3, not > 3

    def test_equilateral_triangle(self):
        self.assertTrue(is_triangle(5, 5, 5))

    def test_zero_or_negative(self):
        self.assertFalse(is_triangle(0, 4, 5))
        self.assertFalse(is_triangle(-1, 4, 5))

    def test_float_values(self):
        self.assertTrue(is_triangle(3.5, 4.2, 5.1))

if __name__ == "__main__":
    unittest.main()
