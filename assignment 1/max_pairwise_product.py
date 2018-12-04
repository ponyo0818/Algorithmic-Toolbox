# python3

def maxPairwiseProductFast(numbers):
    n=len(numbers)
    index1=0
    for i in range(1,n):
        if numbers[i]>numbers[index1]:
            index1=i
    
    index2=0
    for j in range(1,n):
        if numbers[j]==numbers[index1] and j!=index1:
            index2=j
        if numbers[j]!=numbers[index1] and numbers[j]>numbers[index2]:
            index2=j
            

    return numbers[index1]*numbers[index2]



if __name__=='__main__':
    input_n=int(input())
    input_numbers=[int(x) for x in input().split()]
    print(maxPairwiseProductFast(input_numbers))
    