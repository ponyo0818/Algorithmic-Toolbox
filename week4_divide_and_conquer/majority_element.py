# Uses python3

import sys

def get_majority_element(a):
    l=len(a)

    if l==2 :
        if (a[0]==a[1]):
            return a[0]
        else:
            return -1
    elif l==1:
        return a[0]
    #write your code here
    left_array=get_majority_element(a[:l//2])
    right_array=get_majority_element(a[(l//2)+1:])
    
    if(left_array==-1 and right_array>=0):
        return right_array
    elif(right_array==-1 and left_array>=0):
        return left_array
    
    
    if(right_array==left_array):
        return right_array
    else:
        return -1
        

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n=data[0]
    a=data[1:n]
    if get_majority_element(a)!= -1:
        print(1)
    else:
        print(0)
