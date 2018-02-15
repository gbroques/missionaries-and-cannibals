import operator
import unittest

from missionaries_and_cannibals import add_tuples
from missionaries_and_cannibals import contains_negative
from missionaries_and_cannibals import get_actions
from missionaries_and_cannibals import get_initial_state
from missionaries_and_cannibals import get_successors
from missionaries_and_cannibals import has_more_cannibals_than_missionaries
from missionaries_and_cannibals import has_more_than_one_boat
from missionaries_and_cannibals import is_state_valid
from missionaries_and_cannibals import search
from missionaries_and_cannibals import subtract_tuples
from node import Node


class TestMissionariesAndCannibals(unittest.TestCase):
    def test_initial_state(self):
        expected_initial_state = (3, 3, 1)

        initial_state = get_initial_state()

        self.assertEqual(expected_initial_state, initial_state)

    def test_add_lists(self):
        a = (1, 1, 2)
        b = (3, 7, 9)
        expected_list = (4, 8, 11)

        summed_list = add_tuples(a, b)

        self.assertEqual(expected_list, summed_list)

    def test_subtract_lists(self):
        a = (3, 3, 1)
        b = (0, 1, 1)
        expected_list = (3, 2, 0)

        subtracted_list = subtract_tuples(a, b)

        self.assertEqual(expected_list, subtracted_list)

    def test_is_state_valid_with_valid_states(self):
        more_missionaries_than_cannibals = (3, 2, 0)
        equal_number_of_missionaries_and_cannibals = (2, 2, 0)

        self.assertTrue(is_state_valid(more_missionaries_than_cannibals))
        self.assertTrue(is_state_valid(equal_number_of_missionaries_and_cannibals))

    def test_is_state_valid_with_invalid_states(self):
        contains_negative_number = (0, -1, 0)
        more_cannibals_than_missionaries = (2, 3, 0)
        more_than_one_boat = (3, 2, 2)
        more_cannibals_than_initial_state = (4, 3, 1)
        more_missionaries_than_initial_state = (3, 4, 1)

        self.assertFalse(is_state_valid(contains_negative_number))
        self.assertFalse(is_state_valid(more_cannibals_than_missionaries))
        self.assertFalse(is_state_valid(more_than_one_boat))
        self.assertFalse(is_state_valid(more_cannibals_than_initial_state))
        self.assertFalse(is_state_valid(more_missionaries_than_initial_state))

    def test_contains_negative(self):
        self.assertTrue(contains_negative((3, 4, -1)))
        self.assertFalse(contains_negative((3, 4, 0)))

    def test_has_more_than_one_boat(self):
        self.assertTrue(has_more_than_one_boat((3, 3, 2)))
        self.assertFalse(has_more_than_one_boat((3, 3, 1)))

    def test_has_more_cannibals_than_missionaries(self):
        self.assertTrue(has_more_cannibals_than_missionaries((2, 3, 1)))
        self.assertFalse(has_more_cannibals_than_missionaries((2, 2, 1)))

    def test_get_actions(self):
        expected_actions = {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

        actions = get_actions()
        self.assertEqual(expected_actions, actions)

    def test_get_successors_with_subtract_operation(self):
        state = (3, 3, 1)
        expected_successors = {
            (3, 2, 0),
            (3, 1, 0),
            (2, 2, 0)
        }

        successors = get_successors(state, operator.sub)

        self.assertEqual(expected_successors, successors)

    def test_get_successors_with_add_operation(self):
        state = (2, 2, 0)
        expected_successors = {
            (3, 2, 1)
        }

        successors = get_successors(state, operator.add, previous_state=(3, 3, 1))

        self.assertEqual(expected_successors, successors)

    def test_search_at_depth_one(self):
        expected_children = [
            Node((3, 2, 0)),
            Node((3, 1, 0)),
            Node((2, 2, 0))
        ]
        expected_tree = Node((3, 3, 1), expected_children)

        results = search(1)

        self.assertFalse(results['success'])
        self.assertEqual(results['tree'], expected_tree)

    def test_search_at_depth_two(self):
        expected_children = [
            Node((3, 2, 0)),
            Node((3, 1, 0)),
            Node((2, 2, 0))
        ]
        expected_children[1].append(Node((3, 2, 1)))
        expected_children[2].append(Node((3, 2, 1)))
        expected_tree = Node((3, 3, 1), expected_children)

        results = search(2)

        self.assertFalse(results['success'])
        self.assertEqual(results['tree'], expected_tree)

        # From (3, 2, 1) is (3, 0, 0)
        # Then (3, 1, 1)
        # Then (1, 1, 0)
        # Then (2, 2, 1)
        # Then (0, 2, 0)
        # Then (0, 3, 1)

if __name__ == '__main__':
    unittest.main()
