# python3

import sys

def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res



if __name__ == "__main__":
    n = 3
    
    a = [60, 100, 120]
    b = [20, 50, 30]
    max_dot = max_dot_product(a,b)
    print("{:.10f}".format(max_dot)) # print 180.0000000000

# =============================================================================
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     a = data[1:(n + 1)]
#     b = data[(n + 1):]
#     print(max_dot_product(a, b))
# 
# =============================================================================
