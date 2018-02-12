import unittest
import missionaries_and_cannibals


class TestMissionariesAndCannibals(unittest.TestCase):
    def test_initial_state(self):
        expected_initial_state = [3, 3, 1]

        initial_state = missionaries_and_cannibals.get_initial_state()

        self.assertEqual(expected_initial_state, initial_state)

    def test_add_lists(self):
        a = [1, 1, 2]
        b = [3, 7, 9]
        expected_list = [4, 8, 11]

        summed_list = missionaries_and_cannibals.add_lists(a, b)

        self.assertEqual(expected_list, summed_list)

    def test_subtract_lists(self):
        a = [3, 3, 1]
        b = [0, 1, 1]
        expected_list = [3, 2, 0]

        subtracted_list = missionaries_and_cannibals.subtract_lists(a, b)

        self.assertEqual(expected_list, subtracted_list)


if __name__ == '__main__':
    unittest.main()
