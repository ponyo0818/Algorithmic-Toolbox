#Uses python3
#This one is take all the digits in the list to get the maximum value
import sys

def largest_number(a):
    #write your code here
    res=''.join(str(i) for i in a)
    #print(res)
    #print(type(res))
    
    res1=[int(d) for d in res]
    #print(res1)
    res1.sort(reverse=True)
    #print(res1)
    
    res2=''.join(str(j) for j in res1)
    return res2
    
    
    
    #res=nums.sort()
    
    #return res
# =============================================================================
# 
# if __name__ == '__main__':
#     a=[34,56,11]
#     print(largest_number(a))
# =============================================================================
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

