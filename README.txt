Main References for this Assignment
===================================

Stochastic Optimization
-----------------------

** http://www.jhuapl.edu/spsa/PDF-SPSA/Handbook04_StochasticOptimization.pdf (particularly Section 6.3.2 and 6.3.3)

This is how I described doing high-dimensional minimization problems.

Collaborative Filtering
-----------------------

** https://www.coursera.org/learn/machine-learning/lecture/f26nH/collaborative-filtering-algorithm (Lecture 98)
** https://web.stanford.edu/~lmackey/papers/cf_slides-pml09.pdf (only consult this if you don't like Ng's lectures)

If you don't want to learn Stochastic Optimization, then use the Gradient Descent algorithm described
toward the end of Ng's Lecture 98.

I am at present unclear how lambda is meant to be chosen. For now, I just hard-coded it to 1.0.

I also have little feeling for how what Spall calls the gain parameters (alpha_k and c_k) are meant to be chosen,
although Spall gives some suggestions.
