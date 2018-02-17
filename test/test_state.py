import unittest
from state import State


class TestState(unittest.TestCase):
    def test_is_state_valid_with_valid_states(self):
        more_missionaries_than_cannibals = State(3, 2, 0)
        equal_number_of_missionaries_and_cannibals = State(2, 2, 0)

        self.assertTrue(more_missionaries_than_cannibals.is_state_valid())
        self.assertTrue(equal_number_of_missionaries_and_cannibals.is_state_valid())

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

        self.assertFalse(contains_negative_number.is_state_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_wrong_side1.is_state_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_wrong_side2.is_state_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_wrong_side3.is_state_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_right_side1.is_state_valid())
        self.assertFalse(more_cannibals_than_missionaries_on_right_side2.is_state_valid())
        self.assertFalse(more_than_one_boat.is_state_valid())
        self.assertFalse(more_cannibals_than_initial_state.is_state_valid())
        self.assertFalse(more_missionaries_than_initial_state.is_state_valid())


if __name__ == '__main__':
    unittest.main()
