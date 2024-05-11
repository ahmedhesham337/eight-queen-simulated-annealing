from NQueensProblem import NQueensProblem

import random
import numpy as np
import math

import matplotlib.pyplot as plt

def simulated_annealing(state):
    current_state = state
    count = 0

    T = 120
    cooldown_factor = 0.95

    while True:
        count+=1
        cost_current = NQueensProblem.get_cost(current_state)

        if cost_current == 0:
            print(count)
            return current_state
        
        next_state = NQueensProblem.get_random_successor(current_state)
        cost_next  = NQueensProblem.get_cost(next_state)

        delta = cost_next - cost_current

        if (delta <= 0):
            current_state = next_state
        else:
            probability = min(1, math.exp(-delta/T))
            
            if np.random.binomial(1, probability):
                current_state = next_state

        T *= cooldown_factor

def visual(state):
    figure = plt.figure(figsize=(8,8))
    print(state)
    
    tmp = np.array([[1.,0.,1.,0.,1.,0.,1.,0.],
                  [0.,1.,0.,1.,0.,1.,0.,1.],
                  [1.,0.,1.,0.,1.,0.,1.,0.],
                  [0.,1.,0.,1.,0.,1.,0.,1.],
                  [1.,0.,1.,0.,1.,0.,1.,0.],
                  [0.,1.,0.,1.,0.,1.,0.,1.],
                  [1.,0.,1.,0.,1.,0.,1.,0.],
                  [0.,1.,0.,1.,0.,1.,0.,1.]])
    
    for i in range(len(state)):
        tmp[i][state[i]] = 0.4
    
    plt.imshow(tmp, cmap='PRGn')
    plt.axis = False
    plt.show()

def main():
    state = NQueensProblem.get_random_state(8)
    print(state)
    print(NQueensProblem.get_full_board(state))
    sol   = simulated_annealing(state)
    print(NQueensProblem.get_full_board(sol))
    visual(sol)

if __name__ == "__main__":
    main()