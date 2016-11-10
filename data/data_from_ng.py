from collections import namedtuple

# Number of Users
N_U = 4
# Number of Movies
N_M = 5

# In Ng's notation (see lecture titled "Content Based Recommendations" at 06:55):

# r(i, j) == 1 if user j has rated movie i
# y(i, j) = the rating given by user j to movie i

# x[i] is the feature vector for movie i.

# theta[j] is a feature affinity vector for user j (Ng calls the feature affinity vector "parameter vector").
# Personally, I find "parameter vector" a bit vague, since both the theta's and the x's are parameters vectors.

# x[i] is a feature vector for user i


MovieReview = namedtuple("MovieReview", "movie person rating")

# This data is from Ng's course (Lecture 98, 00:24):

MOVIES = ["Love at Last", "Romance Forever", "Cute Puppies of Love", "Nonstop Car Chases", "Swords vs. Karate"]
PEOPLE = ["Alice", "Bob", "Carol", "Dave"]  # Ng's reviewers are numbered 1 to 4. Ours will be numbered 0 to 3.

REVIEWS = [
    # Alice has reviewed four of the five movies.
    MovieReview(0, 0, 5),
    MovieReview(1, 0, 5),
    MovieReview(3, 0, 0),
    MovieReview(4, 0, 0),
    # Bob has reviewed four of the five movies.
    MovieReview(0, 1, 5),
    MovieReview(2, 1, 4),
    MovieReview(3, 1, 0),
    MovieReview(4, 1, 0),
    # Carol has reviewed four of the five movies.
    MovieReview(0, 2, 0),
    MovieReview(2, 2, 0),
    MovieReview(3, 2, 5),
    MovieReview(4, 2, 5),
    # Dave has reviewed three of the five movies.
    MovieReview(0, 3, 0),
    MovieReview(1, 3, 0),
    MovieReview(3, 3, 4),
]
