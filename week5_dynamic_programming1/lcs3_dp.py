#Uses python3
#Dynamic programming implementation of longest common string problem
import sys

#return length of LCS for 
#a[0...m-1], b[0...n-1], and c[0...o-1]
#this idea is to take 3D array to store the length of common subsequence in all 3 
#given sequences


def lcsOfThree(a,b,c,m,n,o):
 
    dp=[[[[0] for i in range(o+1)]for j in range(n+1)]for k in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                            
                if (i==0 or j==0 or k==0):
                    dp[i][j][k]= 0
                
                
                elif (a[i-1]==b[j-1] and b[j-1]==c[k-1]):
                    dp[i][j][k]=1+dp[i-1][j-1][k-1]
                
                else:
                    dp[i][j][k]=max(max(dp[i-1][j][k],
                                        dp[i][j-1][k]),
                                        dp[i][j][k-1])
     
    #dp[m][n][o] contains length of LCS for a,b,c     
    return dp[m][n][o]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcsOfThree(a, b, c,an,bn,cn))
