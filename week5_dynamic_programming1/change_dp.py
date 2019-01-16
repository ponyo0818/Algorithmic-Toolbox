# Uses python3
import sys

def get_change(m):
    #write your code here
    
    denomination=[1,3,4]
    #dp[i]represent the fewest number of coins needed
    dp=[float('inf') for i in range(m+1)]
    #base case
    dp[0]=0
    
    for i in range(1,m+1):
        for coin in denomination:
            if i>=coin:
                #print(dp[i],dp[1-coin],i,coin)
                #dp[i]=min(dp[i-1],dp[i-3],dp[i-4])+1. 1,3,4 are the denomination
                dp[i]=min(dp[i],dp[i-coin]+1)
                #print(dp[i],i)
        print('dp',dp)
    return int(dp[m] if dp[m]!=float('inf')else -1)
    
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
