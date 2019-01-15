# Uses python3
import sys


#Merge two sorted arrays
def Merge(a, b, left, mid, right):
    number_of_inversions = 0
    i, j, k = left, mid, left
    while i <= mid - 1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            #at any step of Merge(), if a[i]is greater than a[j], then there are (mid-i) inversions
            #because left and right subarrays are sorted, so all the remaining elements in left-subarray will
            #be greater than a[j]
            b[k] = a[j]
            j += 1
            number_of_inversions += mid - i
        k += 1
    while i <= mid - 1:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        a[i] = b[i]
    return number_of_inversions

#recursively calls itself to divide the array till size becomes one
#also count the number of inversions
def MergeSort(a, b, left, right):
    number_of_inversions = 0
    if right > left:
        #select the middle point
        mid = (left + right) // 2
        #sum up all the inversions on the left
        number_of_inversions += MergeSort(a, b, left, mid)
        #sum up all the inversions on the right
        number_of_inversions += MergeSort(a, b, mid + 1, right)
        #sum up the inversions that cross between the left and right half
        number_of_inversions += Merge(a, b, left, mid + 1, right)

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0] #b is an empty array of size n
    print(MergeSort(a, b, 0, len(a)-1))
