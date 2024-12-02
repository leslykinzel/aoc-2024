import unittest
from main import is_ordered_and_unique

class TestSequenceValidation(unittest.TestCase):

    def test_is_ascending(self):
        self.assertEqual(is_ordered_and_unique([1, 2, 3]), True)

    def test_is_descending(self):
        self.assertEqual(is_ordered_and_unique([3, 2, 1]), True)

    def test_contains_no_duplicates(self):
        self.assertEqual(is_ordered_and_unique([1, 2, 3]), True)

    def test_contains_duplicates(self):
        self.assertEqual(is_ordered_and_unique([1, 2, 2]), False)

if __name__ == '__main__':
    unittest.main()