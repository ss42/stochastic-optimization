
from random import gauss

from data_from_ng import N, N_M, N_U

# I am very concerned that values too close to zero will result in precision problems

TOO_SMALL = 0.00001


# This does just one number at a time, but it has a guard to guarantee that the number is greater than TOO_SMALL
def generate_perturbation(sigma):
    result = 0.0
    while abs(result) < TOO_SMALL:
        result = gauss(0.0, sigma)

    return result


# This does a whole tuple.
def generate_x_perturbation(sigma):
    # number of components in x is N_M * N
    return tuple([generate_perturbation(sigma) for _ in range(0, N_M * N)])


# This does a whole tuple.
def generate_theta_perturbation(sigma):
    # number of components in theta is N_U * N
    return tuple([generate_perturbation(sigma) for _ in range(0, N_U * N)])
