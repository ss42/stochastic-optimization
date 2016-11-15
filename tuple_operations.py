
# First we implement some basic mathematical operations on tuples.


def inner_product(v1, v2):

    assert len(v1) == len(v2)

    result = 0.0

    for idx in range(len(v1)):
        result += v1[idx] * v2[idx]

    return result


def vector_sum(v, v_perturbation):
    assert len(v) == len(v_perturbation)

    return tuple([x + x_perturbation for x, x_perturbation in zip(v, v_perturbation)])


def vector_difference(v, v_perturbation):
    assert len(v) == len(v_perturbation)

    return tuple([x - x_perturbation for x, x_perturbation in zip(v, v_perturbation)])
