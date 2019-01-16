# Uses python3
import sys

def get_change(m):
    #write your code here
    
    denomination=[1,3,4]
    coins=3 #number of denomination
    
    
    #table[i]will be storing the number of solutions for value i
    #We need n+1 rows as the table is constructed
    #in bottom up manner using the base case (n=0)
    #Initialize all table values as 0
    table=[0 for k in range(m+1)]
    
    #base case when give value is 0
    table[0]=1
    
    #pick all coins one by one and update the table[] values
    #after the index greater than or equal to the value of the picked coin
    
    for i in range(0,coins):
        for j in range(denomination[i],m+1):
            table[j]+=table[j-denomination[i]]
            print ('|i:',i,'|denomination:',denomination[i],'|j:',j,'|table[j]:',table[j])
    return table[m]
    
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
