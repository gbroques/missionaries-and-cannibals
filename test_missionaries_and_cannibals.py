import unittest
import missionaries_and_cannibals


class TestMissionariesAndCannibals(unittest.TestCase):
    def test_initial_state(self):
        expected_initial_state = (3, 3, 1)

        initial_state = missionaries_and_cannibals.get_initial_state()

        self.assertEqual(expected_initial_state, initial_state)

    def test_add_lists(self):
        a = (1, 1, 2)
        b = (3, 7, 9)
        expected_list = (4, 8, 11)

        summed_list = missionaries_and_cannibals.add_tuples(a, b)

        self.assertEqual(expected_list, summed_list)

    def test_subtract_lists(self):
        a = (3, 3, 1)
        b = (0, 1, 1)
        expected_list = (3, 2, 0)

        subtracted_list = missionaries_and_cannibals.subtract_tuples(a, b)

        self.assertEqual(expected_list, subtracted_list)

    def test_is_state_valid(self):
        valid_state1 = (3, 2, 0)
        valid_state2 = (3, 1, 0)
        valid_state3 = (2, 2, 0)

        invalid_state1 = (3, 2, 2)
        invalid_state2 = (0, -1, 13)
        invalid_state3 = (2, 3, 0)
        invalid_state4 = (1, 3, 0)

        self.assertTrue(missionaries_and_cannibals.is_state_valid(valid_state1))
        self.assertTrue(missionaries_and_cannibals.is_state_valid(valid_state2))
        self.assertTrue(missionaries_and_cannibals.is_state_valid(valid_state3))

        self.assertFalse(missionaries_and_cannibals.is_state_valid(invalid_state2))
        self.assertFalse(missionaries_and_cannibals.is_state_valid(invalid_state1))
        self.assertFalse(missionaries_and_cannibals.is_state_valid(invalid_state3))
        self.assertFalse(missionaries_and_cannibals.is_state_valid(invalid_state4))

    def test_contains_negative(self):
        self.assertTrue(missionaries_and_cannibals.contains_negative((3, 4, -1)))
        self.assertFalse(missionaries_and_cannibals.contains_negative((3, 4, 0)))

    def test_has_more_than_one_boat(self):
        self.assertTrue(missionaries_and_cannibals.has_more_than_one_boat((3, 3, 2)))
        self.assertFalse(missionaries_and_cannibals.has_more_than_one_boat((3, 3, 1)))

    def test_has_more_cannibals_than_missionaries(self):
        self.assertTrue(missionaries_and_cannibals.has_more_cannibals_than_missionaries((2, 3, 1)))
        self.assertFalse(missionaries_and_cannibals.has_more_cannibals_than_missionaries((2, 2, 1)))

    def test_get_actions(self):
        expected_actions = {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

        actions = missionaries_and_cannibals.get_actions()
        self.assertEqual(expected_actions, actions)


if __name__ == '__main__':
    unittest.main()
