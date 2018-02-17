from missionaries_and_cannibals import MissionariesAndCannibals
from search import iterative_deepening_search


def main():
    initial_state = get_initial_state()
    goal_state = get_goal_state()
    problem = MissionariesAndCannibals(initial_state, goal_state)
    result = iterative_deepening_search(problem)
    print_path(result.path())


def get_initial_state():
    return 3, 3, 1


def get_goal_state():
    return 0, 0, 0


def print_path(path):
    for node in path:
        print(node.state)


if __name__ == '__main__':
    main()
