# python3
import sys
"""
Created on Wed Dec  5 12:37:29 2018

@author: FY
"""


 
def knapsack(capacity, weights, values):
    value = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            return value
            break
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value


# Driver program to test above function 
# =============================================================================
# val = [60, 100, 120] 
# wt = [10, 20, 30] 
# W = 50
# n = len(val) 
# print(knapSack(W, wt, val, n)) 
# 
# =============================================================================

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = knapsack(capacity, weights, values)
    print("{:.10f}".format(opt_value))
