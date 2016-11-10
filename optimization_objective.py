
# After several motivational lectures, in a lecture titled "Collaborative Filtering Algorithm," at 1:10 Ng reveals
# his optimization objective for collaborative filtering. However, he then simplifies it by having x and theta be
# n-dimensional vectors (where n is the number of features), rather than n+1 dimensional vectors. This leads to a
# simplification discussed in the video about 5:45.

# In this file, we implement optimization_objective. (Ng calls it J.)


def inner_product(v1, v2):

    assert len(v1) == len(v2)

    result = 0.0

    for idx in range(len(v1)):
        result += v1[idx] * v2[idx]

    return result


# As is so often the case in these optimization problems, I will make a function that returns optimization_objective,
# rather than defining optimization_objective directly. This is my way of encapsulating that the function is best
# defined with reviews in its enclosing scope. Globals are messy. Long argument lists are also messy.
# Closures allow us to avoid either of those messes.  Note there is very little cost
# to passing reviews around even if it is a very long list. Its semantic is pass-by-reference, not pass-by-copy.
def make_optimization_objective(lamb, reviews):

    def optimization_objective(x_list, theta_list):
        # Oh boy, here we go.  As you can see at 1:10 of the video, what Ng calls J is decently complex.

        first_sum = 0.0
        second_sum = 0.0
        third_sum = 0.0

        for review in reviews:
            i = review.movie
            j = review.user
            y_i_j = review.rating

            x_i = x_list[i]
            theta_j = theta_list[j]

            delta = inner_product(theta_j, x_i) - y_i_j

            first_sum += delta * delta

        for x in x_list:
            second_sum += inner_product(x, x)

        for theta in theta_list:
            third_sum += inner_product(theta, theta)

        return (first_sum + lamb * second_sum + lamb * third_sum) / 2.0

    return optimization_objective
