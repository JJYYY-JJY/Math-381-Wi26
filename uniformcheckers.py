import numpy as np

# Simulates a Markov chain to estimate the number
# of checkers in a valid n by n checkerboard.
def checkers(n, sample_size=10000, burn=1000):

    # A state is stored as a n by n array, where an
    # entry is 1 if it has a checker and 0 otherwise.

    # Initial state   
    state = np.zeros([n,n], dtype=int)

    # Burn-in stage
    for t in range(burn):
        step(state)

    # For each step after the burn-on period, record
    # the number of checkers in the state.
    checker_count = []
    for t in range(sample_size):
        step(state)
        checker_count.append(np.sum(state))

    # Return the average number of checkers.
    return sum(checker_count) / len(checker_count)


# Performs a step of the Markov chain.
def step(state):
    
    n = len(state)

    # Choose a random square.
    i,j = np.random.choice(n,2)
    
    # If there is already a square at (i,j), remove
    # it and end the step.
    if state[i][j] == 1:
        state[i][j] = 0
        return

    # Check if if is possible to place a sqaure at
    # (i,j); if not, end the step.
    if i > 0:
        if state[i-1][j] == 1:
            return
    if j > 0:
        if state[i][j-1] == 1:
            return
    if i < n-1:
        if state[i+1][j] == 1:
            return 
    if j < n-1:
        if state[i][j+1] == 1:
            return

    # If all checks pass, put a square at (i,j).
    state[i][j] = 1
    return

print(checkers(100))
