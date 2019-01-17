#Uses python3
#Dynamic programming implementation of longest common string problem
import sys

def lcs2(a, b):
    #write your code here
    #Find the length  of the strings
    m=len(a)
    n=len(b)
    
    #declare the array for storing the dp values
    L=[[None]*(n+1) for i in range(m+1)]
    
    #build L[m+1][n+1] in bottom up fashion
    #Note: L[i][j] contains length of LCS of a[0,..,i-1] and b[0,...j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif a[i-1]==b[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    
    return L[i][j]
    
    
    
    return min(len(a), len(b))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
