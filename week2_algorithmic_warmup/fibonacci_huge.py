# python3
def get_fibonacci_huge(n,m):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(n):
            a,b=b,(a+b)%m
        return a
    
n =input()
a, b = map(int, n.split())
print(get_fibonacci_huge(a, b))
