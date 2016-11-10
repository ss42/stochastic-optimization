from data_from_ng import REVIEWS

from optimization_objective import make_optimization_objective


def optimize_ng_example():
    lamb = 1.0  # I'd call this lambda, except in Python that is a keyword. Initialize to 1.0. What should it be?
    optimization_objective_function = make_optimization_objective(lamb, REVIEWS)
    x_list = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]  # i, movie, x
    theta_list = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]  # j, user, theta
    print "Initially, the optimization objective is " + str(optimization_objective_function(x_list, theta_list))


if __name__ == "__main__":
    optimize_ng_example()
