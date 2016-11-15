
# In this file, we test some tuple operations.


import unittest

from simultaneous_perturbation import simultaneous_perturbation

from tuple_operations import inner_product


vector1_for_testing = (3, 5)
vector2_for_testing = (5, 7)

delta1_for_testing = (0.1, 0.2)
delta2_for_testing = (0.2, 0.1)


def optimization_objective_function_for_testing(x_vector, theta_vector):
    return inner_product(x_vector, theta_vector)


class TestSimultaneousPerturbation(unittest.TestCase):

    def test_simultaneous_perturbation(self):
        result_x, result_theta = simultaneous_perturbation(optimization_objective_function_for_testing,
                                                           vector1_for_testing, vector2_for_testing,
                                                           delta1_for_testing, delta2_for_testing)

        we_think_that_prefactor_is_3 = 3
        self.assertAlmostEqual(result_x[0], we_think_that_prefactor_is_3 / delta1_for_testing[0], 7)
        self.assertAlmostEqual(result_theta[1], we_think_that_prefactor_is_3 / delta2_for_testing[1], 7)
