# Uses python3
import sys

# Returns v if v is a majority;
# otherwise, returns None
def get_majority_element(arr, low, high):
  if low == high:
    return arr[low]

  if low + 1 == high:
    return arr[low] if arr[low] == arr[high] else -1

  n = high - low + 1
  mid = (low + high) // 2

  l = get_majority_element(arr, low, mid)
  r = get_majority_element(arr, mid + 1, high)

  #print ('n: ' + str(n) + '; l: ' + str(l) + '; r: ' + str(r) + '; L: ' + str((low, mid)) + '; R: ' + str((mid + 1, high)))

  if l == r:
    return l

  counts = [0, 0]

  for i in range(low, high + 1):
    if arr[i] == l:
      counts[0] = counts[0] + 1
    if arr[i] == r:
      counts[1] = counts[1] + 1

  if l and counts[0] * 2 > n:
    return l

  if r and counts[1] * 2 > n:
    return r

  return -1

#a = [5, 9, 3, 5, 5, 21, 5, 7, 17, 5, 5, 5]

#print (f(a, 0, len(a) - 1))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n=data[0]
    a=data[1:n+1]
    if get_majority_element(a,0,len(a)-1)!= -1:
        print(1)
    else:
        print(0)
