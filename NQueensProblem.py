import numpy as np
import random

class NQueensProblem():

    @staticmethod
    def get_random_state(n):
        return [random.randint(0,n-1) for i in range(n)]

    @staticmethod
    def get_random_successor(state):
        n = len(state)
        successor = state.copy()
        idx = random.randint(0, n-1)
        rr  = random.randint(-successor[idx], n-1-successor[idx])
        while rr == 0:
            rr  = random.randint(-successor[idx], n-1-successor[idx])
        successor[idx] += rr
        return successor

    @staticmethod
    def get_full_board(state):
        n = len(state)
        board = np.zeros((n,n))
        for i in range(len(state)):
            board[i][state[i]] = 1
        return board

    @staticmethod
    def get_cost(state):
        cost = 0
        
        diag_sum = []
        diag_dif = []

        for i in range(len(state)):
            diag_sum.append(i + state[i])
            diag_dif.append(i - state[i])

        for i in range(len(state)):
            for x in range(i+1, len(state)):
                
                if (state[i] == state[x]):
                    cost += 1

                if (diag_sum[i] == diag_sum[x] or diag_dif[i] == diag_dif[x]):
                    cost += 1

        return cost