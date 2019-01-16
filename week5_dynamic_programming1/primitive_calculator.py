# Uses python3
import sys

#dynamic programming
#store all possible parents, work backwards 
def dynamic_sequence(n):
    all_parents=[None]*(n+1)
    all_min_ops=[0]+[None]*n
    
    for k in range(1,n+1):
        #print('k is',k)
        curr_parent=k-1
        curr_min_ops=all_min_ops[curr_parent]+1
        
        if k%3==0:
            parent=k//3
            num_ops=all_min_ops[parent]+1
            if num_ops<curr_min_ops:
                curr_parent,curr_min_ops=parent,num_ops
                
        if k%2==0:
            parent=k//2
            num_ops=all_min_ops[parent]+1
            if num_ops<curr_min_ops:
                curr_parent,curr_min_ops=parent,num_ops
        #print('curr_parent',curr_parent,'curr_min_ops',curr_min_ops)
        
        all_parents[k],all_min_ops[k]=curr_parent,curr_min_ops
        
    numbers=[]
    l=n
    while l>0:
        #append the orgin number at first
        numbers.append(l)
        l=all_parents[l]
    numbers.reverse()
    
    return numbers


input = sys.stdin.read()
n = int(input)
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
