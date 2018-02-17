import unittest

from missionaries_and_cannibals import State


class TestState(unittest.TestCase):
    def test_is_state_valid_with_valid_states(self):
        more_missionaries_than_cannibals = State(3, 2, 0)
        equal_number_of_missionaries_and_cannibals = State(2, 2, 0)

        self.assertTrue(more_missionaries_than_cannibals.is_valid())
        self.assertTrue(equal_number_of_missionaries_and_cannibals.is_valid())

    def test_is_state_valid_with_invalid_states(self):
        contains_negative_number = State(0, -1, 0)
        more_cannibals_than_missionaries_on_wrong_side1 = State(1, 3, 0)
        more_cannibals_than_missionaries_on_wrong_side2 = State(2, 3, 0)
        more_cannibals_than_missionaries_on_wrong_side3 = State(1, 2, 0)
        more_cannibals_than_missionaries_on_right_side1 = State(2, 1, 0)
        more_cannibals_than_missionaries_on_right_side2 = State(1, 0, 0)
        more_than_one_boat = State(3, 2, 2)
        more_cannibals_than_initial_state = State(4, 3, 1)
        more_missionaries_than_initial_state = State(3, 4, 1)

        self.assertFalse(contains_negative_number.is_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_wrong_side1.is_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_wrong_side2.is_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_wrong_side3.is_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_right_side1.is_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_right_side2.is_valid())
        self.assertFalse(more_than_one_boat.is_valid())
        self.assertFalse(more_cannibals_than_initial_state.is_valid())
        self.assertFalse(more_missionaries_than_initial_state.is_valid())

    def test_add(self):
        expected_result = State(3, 1, 4)
        a = State(1, 0, 1)
        b = State(2, 1, 3)
        result = a + b

        self.assertEqual(expected_result, result)

    def test_add_with_tuple(self):
        expected_result = State(3, 1, 4)
        a = State(1, 0, 1)
        b = (2, 1, 3)
        result = a + b

        self.assertEqual(expected_result, result)

    def test_add_raises_value_error_with_invalid_operand(self):
        a = State(1, 0, 1)
        b = "invalid operand"
        with self.assertRaises(ValueError):
            a + b

    def test_subtract(self):
        expected_result = State(2, 2, 0)
        a = State(3, 3, 1)
        b = State(1, 1, 1)
        result = a - b

        self.assertEqual(expected_result, result)

    def test_subtract_with_tuple(self):
        expected_result = State(2, 2, 0)
        a = State(3, 3, 1)
        b = (1, 1, 1)
        result = a - b
        self.assertEqual(expected_result, result)

    def test_subtract_raises_value_error_with_invalid_operand(self):
        a = State(3, 3, 1)
        b = "invalid operand"
        with self.assertRaises(ValueError):
            a - b

    def test_less_than(self):
        a = State(3, 3, 0)
        b = State(3, 3, 1)
        self.assertTrue(a < b)

    def test_less_than_raises_value_error_with_invalid_operand(self):
        a = State(3, 3, 0)
        b = (3, 3, 1)
        with self.assertRaises(ValueError):
            a < b

    def test_equal(self):
        a = State(3, 3, 1)
        b = State(3, 3, 1)
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
