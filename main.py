from missionaries_and_cannibals import MissionariesAndCannibals
from search import iterative_deepening_search


def main():
    problem = MissionariesAndCannibals()
    result = iterative_deepening_search(problem)
    print_path(result.path())


def print_path(path):
    for node in path:
        print(node.state.value)


if __name__ == '__main__':
    main()
