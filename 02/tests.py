import unittest
from main import ordered_and_unique, spaced_within

class TestSequenceValidation(unittest.TestCase):

    def test_order_ascending(self):
        self.assertEqual(ordered_and_unique([1, 2, 3, 4, 5]), True)

    def test_order_descending(self):
        self.assertEqual(ordered_and_unique([5, 4, 3, 2, 1]), True)

    def test_all_unique(self):
        self.assertEqual(ordered_and_unique([1, 2, 3, 4, 5]), True)

    def test_not_all_unique(self):
        self.assertEqual(ordered_and_unique([1, 2, 2, 4, 5]), False)

    def test_1_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 2, 3, 4, 5], 3), True)

    def test_1_spacing_descending(self):
        self.assertEqual(spaced_within([5, 4, 3, 2, 1], 3), True)

    def test_2_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 3, 5, 7, 9], 3), True)

    def test_2_spacing_descending(self):
        self.assertEqual(spaced_within([9, 7, 5, 3, 1], 3), True)

    def test_3_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 4, 7, 10, 13], 3), True)

    def test_3_spacing_descending(self):
        self.assertEqual(spaced_within([13, 10, 7, 4, 1], 3), True)

    def test_4_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 5, 9, 13, 17], 3), False)

    def test_4_spacing_descending(self):
        self.assertEqual(spaced_within([17, 13, 9, 5, 1], 3), False)

if __name__ == '__main__':
    unittest.main()
