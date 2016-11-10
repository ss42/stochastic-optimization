
# After several motivational lectures, in a lecture titled "Collaborative Filtering Algorithm," at 1:10 Ng reveals
# his optimization objective for collaborative filtering.

# In this file, we implement the optimization objective, which I will call o_o, although he calls it J.


# As is so often the case, I will actually make a function that will return o_o.
def make_o_o(lamb, reviews):

    def o_o(x_list, theta_list):
        # Oh boy, here we go.  As you can see at 1:10 of the video, what Ng calls J is decently complex.

        first_sum = 0.0
        second_sum = 0.0
        third_sum = 0.0

        for _ in reviews:
            pass

        for _ in x_list:
            pass

        for _ in theta_list:
            pass

        return (first_sum + lamb * second_sum + lamb * third_sum) / 2.0

    return o_o
