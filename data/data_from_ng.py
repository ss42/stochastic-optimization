from collections import namedtuple

MovieReview = namedtuple("MovieReview", "movie person rating")

# This data is from Ng's course (Lecture 98, 00:24):

MOVIES = ["Love at Last", "Romance Forever", "Cute Puppies of Love", "Nonstop Car Chases", "Swords vs. Karate"]
PEOPLE = ["Alice", "Bob", "Carol", "Dave"]

REVIEWS = [
    # Alice
    MovieReview(0, 0, 5),
    MovieReview(1, 0, 5),
    MovieReview(3, 0, 0),
    MovieReview(4, 0, 0),
    # Bob
    MovieReview(0, 1, 5),
    MovieReview(2, 1, 4),
    MovieReview(3, 1, 0),
    MovieReview(4, 1, 0),
    # Carol
    MovieReview(0, 2, 0),
    MovieReview(2, 2, 0),
    MovieReview(3, 2, 5),
    MovieReview(4, 2, 5),
    # Dave
    MovieReview(0, 3, 0),
    MovieReview(1, 3, 0),
    MovieReview(3, 3, 4),
]
