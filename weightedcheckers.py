import numpy as np

# Simulates a Metropolis chain to estimate the number
# of checkers in a valid n by b checkerboard, with
# distribution proportional to l^(number of checkers).
def checkers(n, l, sample_size=10000, burn=1000):
    
    # A state is stored as a n by n array, where an
    # entry is 1 if it has a checker and 0 otherwise.

    # Initial state
    state = np.zeros([n,n], dtype=int)

    # Burn-in stage
    for t in range(burn):
        step(state, l)

    # For each step after the burn-on period, record
    # the number of checkers in the state.
    checker_counts = []
    for t in range(sample_size):
        step(state, l)
        checker_counts.append(np.sum(state))

    # Return the average number of checkers.
    return sum(checker_counts) / len(checker_counts)


# Performs a step of the Metropolis chain.
def step(state, l):
    
    n = len(state)

    # Choose a random square.
    i,j = np.random.choice(n,2)

    # Use the proposal chain to propose a new state.
    # The proposed state agrees with the current
    # state everywhere except (i,j), so for
    # efficiency we only store the proposed value
    # at (i,j).
    proposalij = 1    
    if state[i][j] == 1:
        proposalij = 0
    else:
        if i > 0:
            if state[i-1][j] == 1:
                proposalij = 0
        if j > 0:
            if state[i][j-1] == 1:
                proposalij = 0
        if i < n-1:
            if state[i+1][j] == 1:
                proposalij = 0 
        if j < n-1:
            if state[i][j+1] == 1:
                proposalij = 0

    # Decide whether to accept the proposal. Since
    # the proposed state agrees with the current state
    # except at (i,j), we only need to calculate
    # proposalij - state[i][j].
    alpha = float(l) ** (proposalij - state[i][j])
    r = np.random.rand()
    if r < alpha:
        state[i][j] = proposalij 
    
    return
        

print(checkers(8,1))