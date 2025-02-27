import unittest
from main import *

operators = [ '+', '*', '||' ]
targets = [190, 3267, 83, 156, 7290, 161011, 192, 21037, 292]
factors = [
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

class TestListProcessing(unittest.TestCase):

    def test_get_all_possible_expressions(self):
        '''
            Given a list of integers, get_all_possible_expressions() should return 
            a list of possible expressions based on the operators passed by the caller.
        '''
        expected = [
            [[10, '+', 19], [10, '*', 19], [10, '||', 19]], 
            [[81, '+', 40, '+', 27], [81, '+', 40, '*', 27], [81, '+', 40, '||', 27], [81, '*', 40, '+', 27], [81, '*', 40, '*', 27], [81, '*', 40, '||', 27], [81, '||', 40, '+', 27], [81, '||', 40, '*', 27], [81, '||', 40, '||', 27]], 
            [[17, '+', 5], [17, '*', 5], [17, '||', 5]], [[15, '+', 6], [15, '*', 6], [15, '||', 6]], 
            [[6, '+', 8, '+', 6, '+', 15], [6, '+', 8, '+', 6, '*', 15], [6, '+', 8, '+', 6, '||', 15], [6, '+', 8, '*', 6, '+', 15], [6, '+', 8, '*', 6, '*', 15], [6, '+', 8, '*', 6, '||', 15], [6, '+', 8, '||', 6, '+', 15], [6, '+', 8, '||', 6, '*', 15], [6, '+', 8, '||', 6, '||', 15], [6, '*', 8, '+', 6, '+', 15], [6, '*', 8, '+', 6, '*', 15], [6, '*', 8, '+', 6, '||', 15], [6, '*', 8, '*', 6, '+', 15], [6, '*', 8, '*', 6, '*', 15], [6, '*', 8, '*', 6, '||', 15], [6, '*', 8, '||', 6, '+', 15], [6, '*', 8, '||', 6, '*', 15], [6, '*', 8, '||', 6, '||', 15], [6, '||', 8, '+', 6, '+', 15], [6, '||', 8, '+', 6, '*', 15], [6, '||', 8, '+', 6, '||', 15], [6, '||', 8, '*', 6, '+', 15], [6, '||', 8, '*', 6, '*', 15], [6, '||', 8, '*', 6, '||', 15], [6, '||', 8, '||', 6, '+', 15], [6, '||', 8, '||', 6, '*', 15], [6, '||', 8, '||', 6, '||', 15]], 
            [[16, '+', 10, '+', 13], [16, '+', 10, '*', 13], [16, '+', 10, '||', 13], [16, '*', 10, '+', 13], [16, '*', 10, '*', 13], [16, '*', 10, '||', 13], [16, '||', 10, '+', 13], [16, '||', 10, '*', 13], [16, '||', 10, '||', 13]], 
            [[17, '+', 8, '+', 14], [17, '+', 8, '*', 14], [17, '+', 8, '||', 14], [17, '*', 8, '+', 14], [17, '*', 8, '*', 14], [17, '*', 8, '||', 14], [17, '||', 8, '+', 14], [17, '||', 8, '*', 14], [17, '||', 8, '||', 14]], 
            [[9, '+', 7, '+', 18, '+', 13], [9, '+', 7, '+', 18, '*', 13], [9, '+', 7, '+', 18, '||', 13], [9, '+', 7, '*', 18, '+', 13], [9, '+', 7, '*', 18, '*', 13], [9, '+', 7, '*', 18, '||', 13], [9, '+', 7, '||', 18, '+', 13], [9, '+', 7, '||', 18, '*', 13], [9, '+', 7, '||', 18, '||', 13], [9, '*', 7, '+', 18, '+', 13], [9, '*', 7, '+', 18, '*', 13], [9, '*', 7, '+', 18, '||', 13], [9, '*', 7, '*', 18, '+', 13], [9, '*', 7, '*', 18, '*', 13], [9, '*', 7, '*', 18, '||', 13], [9, '*', 7, '||', 18, '+', 13], [9, '*', 7, '||', 18, '*', 13], [9, '*', 7, '||', 18, '||', 13], [9, '||', 7, '+', 18, '+', 13], [9, '||', 7, '+', 18, '*', 13], [9, '||', 7, '+', 18, '||', 13], [9, '||', 7, '*', 18, '+', 13], [9, '||', 7, '*', 18, '*', 13], [9, '||', 7, '*', 18, '||', 13], [9, '||', 7, '||', 18, '+', 13], [9, '||', 7, '||', 18, '*', 13], [9, '||', 7, '||', 18, '||', 13]], 
            [[11, '+', 6, '+', 16, '+', 20], [11, '+', 6, '+', 16, '*', 20], [11, '+', 6, '+', 16, '||', 20], [11, '+', 6, '*', 16, '+', 20], [11, '+', 6, '*', 16, '*', 20], [11, '+', 6, '*', 16, '||', 20], [11, '+', 6, '||', 16, '+', 20], [11, '+', 6, '||', 16, '*', 20], [11, '+', 6, '||', 16, '||', 20], [11, '*', 6, '+', 16, '+', 20], [11, '*', 6, '+', 16, '*', 20], [11, '*', 6, '+', 16, '||', 20], [11, '*', 6, '*', 16, '+', 20], [11, '*', 6, '*', 16, '*', 20], [11, '*', 6, '*', 16, '||', 20], [11, '*', 6, '||', 16, '+', 20], [11, '*', 6, '||', 16, '*', 20], [11, '*', 6, '||', 16, '||', 20], [11, '||', 6, '+', 16, '+', 20], [11, '||', 6, '+', 16, '*', 20], [11, '||', 6, '+', 16, '||', 20], [11, '||', 6, '*', 16, '+', 20], [11, '||', 6, '*', 16, '*', 20], [11, '||', 6, '*', 16, '||', 20], [11, '||', 6, '||', 16, '+', 20], [11, '||', 6, '||', 16, '*', 20], [11, '||', 6, '||', 16, '||', 20]]
        ]

        for i in range(len(factors)):
            self.assertEqual(get_all_possible_expressions(factors[i], operators), expected[i])

    def test_eval_concat_operator(self):
        '''
            A list containing a mathematical expression must be
            evaluated left to right ignoring any operator precedence.
        '''
        test_cases = [
            [10, '*', 19],
            [81, '+', 40, '*', 27],
            [156],
            [178, '+', 14],
            [11, '+', 6, '*', 16, '+', 20],
            [6, '*', 8, '||', 6, '*', 15],
            [17, '||', 8, '+', 14]
        ]
        expected = [
            190,
            3267,
            156,
            192,
            292,
            7290,
            192
        ]

        for i in range(len(test_cases)):
            print(f'Expected:{expected[i]}')
            print(f'Actual: {eval_left_to_right(test_cases[i])}')
            self.assertEqual(eval_left_to_right(test_cases[i]), expected[i])


if __name__ == '__main__':
    unittest.main()
