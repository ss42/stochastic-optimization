
# In this file, we test some tuple operations.


import unittest

from tuple_operations import vector_sum, vector_difference, inner_product


vector1_for_testing = (3, 5)
vector2_for_testing = (5, 7)


class TestNewtonsMethod(unittest.TestCase):

    def test_vector_sum(self):
        vector1_plus_vector2 = vector_sum(vector1_for_testing, vector2_for_testing)
        self.assertEqual((8, 12), vector1_plus_vector2)

    def test_vector_difference(self):
        vector1_minus_vector2 = vector_difference(vector2_for_testing, vector1_for_testing)
        self.assertEqual((2, 2), vector1_minus_vector2)

    def test_inner_product(self):
        vector1_inner_product_vector2 = inner_product(vector2_for_testing, vector1_for_testing)
        expected_inner_product = 50
        self.assertEqual(vector1_inner_product_vector2, expected_inner_product)
