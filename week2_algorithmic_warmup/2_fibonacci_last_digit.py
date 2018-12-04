# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(n):
            a,b=b%10,(a+b)%10
        return a%10 #calculate the reminder after divided 10
    
n = int(input())
print(get_fibonacci_last_digit_naive(n))
