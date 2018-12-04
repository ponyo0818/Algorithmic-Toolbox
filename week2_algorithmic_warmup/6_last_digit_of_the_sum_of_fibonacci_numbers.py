# Uses python3

def get_sum_fibonacci_last_digit(n):
    if n<2:return n
    else:
        sum_,a,b=1,0,1
        for i in range(1,n%60):
            a,b=b,(a+b)%10
            sum_=(sum_+b)%10
        return sum_ #calculate the reminder after divided 10
    
n = int(input())
print(get_sum_fibonacci_last_digit(n))
