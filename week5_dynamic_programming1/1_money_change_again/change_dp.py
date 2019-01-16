# Uses python3
import sys

def get_change(m):
    #write your code here
    #Variables for number of coins and the array of coins's type
    numberOfCoins=3
    coins=[1,3,4]
    min_coins=[0]+[sys.maxsize]*m
    
    for i in range(1,numberOfCoins+1):
        for j in range(coins[i-1],m+1):
            min_coins[j]=min(min_coins[j-coins[i-1]]+1,min_coins[j])
            
    return min_coins
    
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
