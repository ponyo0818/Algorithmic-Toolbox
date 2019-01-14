# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    left_array=get_majority_element(a,left,(left+right-1)//2+1)
    right_array=get_majority_element(a,(left+right-1)//2+1,right)
    
    lcount=0
    for i in range(left,right):
        if a[i]==left_array:
            lcount+=1
    if lcount>(right-left)//2:
        return left_array
    
    rcount=0
    for j in range(left,right):
        if a[i]==right_array:
            rcount+=1
    if rcount>(right-left)//2:
        return right_array
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
