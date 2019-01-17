# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    K=[[0 for x in range(W+1)] for x in range(len(w)+1)]
    for i in range(len(w)+1):
        for j in range(W+1):
            if (i==0 or j==0):
                K[i][j]=0
            elif w[i-1]<=j:
                K[i][j]=max(w[i-1]+K[i-1][j-w[i-1]],K[i-1][j])
            else:
                K[i][j]=K[i-1][j]
    return K[n][W]
                

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
