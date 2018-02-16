import unittest

from main import get_goal_state
from main import get_initial_state
from missionaries_and_cannibals import MissionariesAndCannibals


class TestMissionariesAndCannibals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initial_state = get_initial_state()
        goal_state = get_goal_state()
        cls.problem = MissionariesAndCannibals(initial_state, goal_state)

    def test_is_state_valid_with_valid_states(self):
        more_missionaries_than_cannibals = (3, 2, 0)
        equal_number_of_missionaries_and_cannibals = (2, 2, 0)

        self.assertTrue(self.problem.is_state_valid(more_missionaries_than_cannibals))
        self.assertTrue(self.problem.is_state_valid(equal_number_of_missionaries_and_cannibals))

    def test_is_state_valid_with_invalid_states(self):
        contains_negative_number = (0, -1, 0)
        more_cannibals_than_missionaries = (2, 3, 0)
        more_than_one_boat = (3, 2, 2)
        more_cannibals_than_initial_state = (4, 3, 1)
        more_missionaries_than_initial_state = (3, 4, 1)

        self.assertFalse(self.problem.is_state_valid(contains_negative_number))
        self.assertFalse(self.problem.is_state_valid(more_cannibals_than_missionaries))
        self.assertFalse(self.problem.is_state_valid(more_than_one_boat))
        self.assertFalse(self.problem.is_state_valid(more_cannibals_than_initial_state))
        self.assertFalse(self.problem.is_state_valid(more_missionaries_than_initial_state))

    def test_contains_negative(self):
        self.assertTrue(self.problem.contains_negative((3, 4, -1)))
        self.assertFalse(self.problem.contains_negative((3, 4, 0)))

    def test_has_more_than_one_boat(self):
        self.assertTrue(self.problem.has_more_than_one_boat((3, 3, 2)))
        self.assertFalse(self.problem.has_more_than_one_boat((3, 3, 1)))

    def test_has_more_cannibals_than_missionaries(self):
        self.assertTrue(self.problem.has_more_cannibals_than_missionaries((2, 3, 1)))
        self.assertFalse(self.problem.has_more_cannibals_than_missionaries((2, 2, 1)))

    def test_get_all_actions(self):
        expected_actions = {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

        actions = self.problem.get_all_actions()
        self.assertEqual(expected_actions, actions)

    def test_actions_from_initial_state(self):
        expected_actions = {
            (0, 1, 1),
            (1, 1, 1),
            (0, 2, 1)
        }

        actions = self.problem.actions((3, 3, 1))

        self.assertEquals(expected_actions, actions)

    def test_actions_from_second_state(self):
        expected_actions = {
            (1, 0, 1),
            (1, 1, 1)
        }

        actions = self.problem.actions((2, 2, 0))

        self.assertEquals(expected_actions, actions)

    def test_result_on_initial_transition(self):
        expected_result = (2, 2, 0)
        state = (3, 3, 1)
        action = (1, 1, 1)

        result = self.problem.result(state, action)

        self.assertEqual(expected_result, result)

    def test_result_on_second_transition(self):
        expected_result = (3, 2, 1)
        state = (2, 2, 0)
        action = (1, 0, 1)

        result = self.problem.result(state, action)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
