class Node:
    def __init__(self, state=(3, 3, 1), children=None):
        self.state = state
        self.children = []
        if children is not None:
            for child in children:
                self.append(child)

    def append(self, state):
        assert isinstance(state, Node)
        self.children.append(state)

    def __eq__(self, other):
        if self.state != other.state:
            return False
        elif self.children != other.children:
            return False
        else:
            return True
