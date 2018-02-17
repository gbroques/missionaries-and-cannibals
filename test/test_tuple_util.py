import unittest

from util import add_tuples
from util import contains_negative
from util import subtract_tuples


class TestTupleUtil(unittest.TestCase):
    def test_add_tuples(self):
        a = (1, 1, 2)
        b = (3, 7, 9)
        expected_list = (4, 8, 11)

        summed_list = add_tuples(a, b)

        self.assertEqual(expected_list, summed_list)

    def test_subtract_tuples(self):
        a = (3, 3, 1)
        b = (0, 1, 1)
        expected_list = (3, 2, 0)

        subtracted_list = subtract_tuples(a, b)

        self.assertEqual(expected_list, subtracted_list)

    def test_contains_negative(self):
        self.assertTrue(contains_negative((3, 4, -1)))
        self.assertFalse(contains_negative((3, 4, 0)))


if __name__ == '__main__':
    unittest.main()
