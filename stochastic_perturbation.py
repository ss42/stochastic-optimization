
from random import gauss

from data_from_ng import N, N_M, N_U

# I am very concerned that values too close to zero will result in precision problems

TOO_SMALL = 0.00001


# This does just one number at a time, but it has a guard to guarantee that the number is greater than TOO_SMALL
def generate_scalar_perturbation(sigma):
    result = 0.0
    while abs(result) < TOO_SMALL:
        result = gauss(0.0, sigma)

    return result


# This does a tuple
def generate_tuple_perturbation(sigma):
    return tuple([generate_scalar_perturbation(sigma) for _ in range(0, N)])


# This does N_M tuples
def generate_x_perturbation(sigma):
    # number of components in x is N_M
    return [generate_scalar_perturbation(sigma) for _ in range(0, N_M)]


# This does N_U tuples
def generate_theta_perturbation(sigma):
    # number of components in theta is N_U
    return [generate_perturbation(sigma) for _ in range(0, N_U)]


# This does a whole perturbation all at once for all of the (N_M + N_U) * N components
def generate_perturbation(sigma):
    return generate_x_perturbation(sigma), generate_theta_perturbation(sigma)
