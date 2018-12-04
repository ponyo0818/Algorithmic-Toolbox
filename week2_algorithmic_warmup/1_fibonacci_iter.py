# python 3

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
# =============================================================================
# 
# for i in range(100):
#     print(fib(i))
# 
#     
# =============================================================================
n = int(input())
print(fib(n))
