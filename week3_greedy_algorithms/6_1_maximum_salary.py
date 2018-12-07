# python3

import sys

def largest_number(a):
    #write your code here
    a=list(map(int,a))
    result=sorted(a,key=fractionalize,reverse=True)
    res=''.join(str(j) for j in result)
    return res

def fractionalize(i):
    divisor=9
    while divisor<i:
        divisor=10*divisor+9
    return i/divisor

# =============================================================================
# if __name__ == '__main__':
#      a=[34,56,11]
#      print(largest_number(a))
#      
# =============================================================================
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

