# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while left<=right:
        mid=left+(right-left)//2
        
        #if element is present at the middle itself
        if a[mid]==x:
            return mid        
           
        #if element is smaller than mid, then it can only be present in left subarray
        elif a[mid]>x:
            right=mid-1
        #if element is greater than mid, then it can only be present i right subarray
        else:
            left=mid+1
    return -1
            

            
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')





