import operator


def add_tuples(a, b):
    return operate_on_tuples(a, b, operator.add)


def subtract_tuples(a, b):
    return operate_on_tuples(a, b, operator.sub)


def operate_on_tuples(a, b, operation):
    return tuple(map(operation, a, b))


def contains_negative(collection):
    """Return True if any negative value exists in the collection."""
    return any(n < 0 for n in collection)
