import unittest
from main import ordered_and_unique, spaced_within

class TestSequenceValidation(unittest.TestCase):

    def test_is_ascending(self):
        self.assertEqual(ordered_and_unique([1, 2, 3]), True)

    def test_is_descending(self):
        self.assertEqual(ordered_and_unique([3, 2, 1]), True)

    def test_contains_no_duplicates(self):
        self.assertEqual(ordered_and_unique([1, 2, 3]), True)

    def test_contains_duplicates(self):
        self.assertEqual(ordered_and_unique([1, 2, 2]), False)

    def test_1_spacing_descending(self):
        self.assertEqual(spaced_within([3, 2, 1], 3), True)

    def test_1_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 2, 3], 3), True)

    def test_1_spacing_descending(self):
        self.assertEqual(spaced_within([3, 2, 1], 3), True)

    def test_2_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 3, 5], 3), True)

    def test_2_spacing_descending(self):
        self.assertEqual(spaced_within([5, 3, 1], 3), True)

    def test_3_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 4, 7], 3), True)

    def test_3_spacing_descending(self):
        self.assertEqual(spaced_within([7, 4, 1], 3), True)

    def test_4_spacing_ascending(self):
        self.assertEqual(spaced_within([1, 5, 9], 3), False)

    def test_4_spacing_descending(self):
        self.assertEqual(spaced_within([9, 5, 1], 3), False)

if __name__ == '__main__':
    unittest.main()