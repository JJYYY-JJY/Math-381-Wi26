# Please refer to the coffee shop example we did in lecture.

import numpy as np

# P is the transition probability matrix, q is the initial
# distribution. Please note the double bracketing in the
# definition of P.
P = np.array([[0.3,0.7],[0.6,0.4]])
q = np.array([0,1])


# Compute q*P^k, which gives the distribution of X_k.
k = 10000
r = q @ np.linalg.matrix_power(P, k)

print(r)


# Finds the stationary distribution of the Markov chain by solving
# a system of equations.
A = np.identity(2) - P.T           # Creates the matrix of coefficients
A = np.append(A, [[1,1]], axis=0)  # Appends the additional equation x1+x2=1
b = [0,0,1]                        # Right hand side
x = np.linalg.lstsq(A,b)[0]  # We use the lstsq function to solve, since A
                             # is not a square matrix.
print(x)