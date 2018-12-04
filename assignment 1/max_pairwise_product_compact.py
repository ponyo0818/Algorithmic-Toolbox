# python3


def maxPairwiseProductBySorting(numbers):
    newlist=sorted(numbers)
    return newlist[-1]*newlist[-2]

if __name__=='__main__':
    input_n=int(input())
    input_numbers=[int(x) for x in input().split()]
    print(maxPairwiseProductBySorting(input_numbers))
    