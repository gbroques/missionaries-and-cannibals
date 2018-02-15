class Node:
    """
    A node in a search tree. Contains a pointer to the parent,
    and the actual state of the node.

    Source: https://github.com/aimacode/aima-python/blob/master/search.py
    """
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
            return list(reversed(path_back))

    def __repr__(self):
        return '<Node {}>'.format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def __str__(self):
        return '<Node {}>'.format(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)
