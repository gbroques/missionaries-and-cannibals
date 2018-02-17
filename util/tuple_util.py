import operator


def add_tuples(a, b):
    return operate_on_tuples(a, b, operator.add)


def subtract_tuples(a, b):
    return operate_on_tuples(a, b, operator.sub)


def operate_on_tuples(a, b, operation):
    return tuple(map(operation, a, b))
