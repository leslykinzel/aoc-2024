import unittest
from main import *

class TestListProcessing(unittest.TestCase):

    def __init__(self):
        self.operators = [ '+', '*', '||' ]
        self.targets = [190, 3267, 83, 156, 7290, 161011, 192, 21037, 292]
        self.factors = [
            [10, 19],
            [81, 40, 27],
            [17, 5],
            [15, 6],
            [6, 8, 6, 15],
            [16, 10, 13],
            [17, 8, 14],
            [9, 7, 18, 13],
            [11, 6, 16, 20]
        ]

    def test_get_all_possible_expressions(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
