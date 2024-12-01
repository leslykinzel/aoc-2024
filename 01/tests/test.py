import unittest
from main import get_distance

class TestGetDistance(unittest.TestCase):

    def test_x_greater_than_y(self):
        self.assertEqual(get_distance(5, 3), 2)

    def test_y_greater_than_x(self):
        self.assertEqual(get_distance(3, 5), 2)

    def test_x_equal_to_y(self):
        self.assertEqual(get_distance(5, 5), 0)

    def test_x_negative(self):
        self.assertEqual(get_distance(-5, 3), 8)

    def test_y_negative(self):
        self.assertEqual(get_distance(3, -5), 8)

    def test_both_negative(self):
        self.assertEqual(get_distance(-5, -3), 2)

    def test_x_zero(self):
        self.assertEqual(get_distance(0, 5), 5)

    def test_y_zero(self):
        self.assertEqual(get_distance(5, 0), 5)

    def test_both_zero(self):
        self.assertEqual(get_distance(0, 0), 0)

if __name__ == '__main__':
    unittest.main()