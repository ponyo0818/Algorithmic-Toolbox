# python3
def lastdigit_square(n):
    return (fib(n)*fib(n+1))%10


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a
n = int(input())
print(lastdigit_square(n))
    
