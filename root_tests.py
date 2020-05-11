import unittest
from square_root import root


class TestStringMethods(unittest.TestCase):

    def test_positive_root(self):
        res = root(4, precision=2)
        self.assertEqual(res, (0, '+- 2.00'))

    def test_negative_root(self):
        res = root(-4, precision=2)
        self.assertEqual(res, (0, '+- 2.00i'))

    def test_zero_root(self):
        res = root(0, precision=2)
        self.assertEqual(res, (0, '0.00'))

    def test_invalid_number(self):
        res = root('abs', precision=2)
        self.assertEqual(res, (1, None))

    def test_invalid_precision(self):
        res = root(1, precision='abs')
        self.assertEqual(res, (2, None))

    def test_out_of_range_number(self):
        res = root('10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', precision=2)
        self.assertEqual(res, (3, None))

    def test_out_of_range_precision_small(self):
        res = root(1, precision='0')
        self.assertEqual(res, (4, None))

    def test_out_of_range_precision_big(self):
        res = root(1, precision='51')
        self.assertEqual(res, (4, None))

    def test_max_possible_root(self):
        res = root('9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999', precision=2)
        self.assertEqual(res[0], 0)

    def test_min_possible_root(self):
        res = root('-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999', precision=2)
        self.assertEqual(res[0], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
