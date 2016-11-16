
# First we implement some basic mathematical operations on tuples.


def tuple_inner_product(v1, v2):

    assert len(v1) == len(v2)

    result = 0.0

    for idx in range(len(v1)):
        result += v1[idx] * v2[idx]

    return result


def tuple_sum(v, v_perturbation):
    assert len(v) == len(v_perturbation)

    return tuple([x + x_perturbation for x, x_perturbation in zip(v, v_perturbation)])


def tuple_difference(v, v_perturbation):
    assert len(v) == len(v_perturbation)

    return tuple([x - x_perturbation for x, x_perturbation in zip(v, v_perturbation)])


# Wow, now we need operations on vectors of tuples!

def vector_sum(x, x_perturbation):
    assert len(x) == len(x_perturbation)

    return [tuple_sum(x_tuple, x_tuple_perturbation) for x_tuple, x_tuple_perturbation in zip(x, x_perturbation)]


def vector_difference(x, x_perturbation):
    assert len(x) == len(x_perturbation)

    return [tuple_difference(x_tuple, x_tuple_perturbation) for x_tuple, x_tuple_perturbation in zip(x, x_perturbation)]
