# Uses python3

def get_sum_fibonacci_last_digit(m,n):
    if n<=2:return n
    else:
        a,b=0,1
        if (m<2):sum_=1
        else: sum_=0

        for i in range(1,n%60):
            #print('i is',i)
            a,b=b,(a+b)%10
            #print('b is',b)
            if i>=(m-1):
                sum_=(sum_+b)%10
                #print('sum',sum_)
        return sum_ #calculate the reminder after divided 10
    
m,n = map(int, input().split()) 
print(get_sum_fibonacci_last_digit(m,n))
