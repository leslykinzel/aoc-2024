import unittest
from main import concat_ints, left_to_right_eval

class TestListProcessing(unittest.TestCase):

    def test_concat_ints(self):
        self.assertEqual(concat_ints(123, 456), 123456)

    def test_list_ops(self):
        self.assertEqual(left_to_right_eval([10, 19], ['*']), 190)

    def test_list_eval_1(self):
        self.assertEqual(left_to_right_eval([10, 19], ['+']), 29)

    def test_list_eval_2(self):
        self.assertEqual(left_to_right_eval([10, 19], ['||']), 1019)

    def test_list_eval_3(self):
        self.assertEqual(left_to_right_eval([81, 40, 27], ['*', '||']), (81 * 4027))

if __name__ == '__main__':
    unittest.main()
