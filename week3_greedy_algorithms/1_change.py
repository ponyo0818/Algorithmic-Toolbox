# Uses python3


def get_change(m):
    #write your code here
    #denominations:1,5,10
    A=[] #number of each coin
    B=[10,5,1]
    n=3
    for i in range(0,n):
        print('i is: ',i)
        if m==0:
            return A
        elif B[i]<=m:
            number=int(m/B[i]) #number of each coin
            print('number and coin value is:',number, B[i])
            m=m-number*B[i] #what's left
            print('m is: ',m)
            A.append(number)
            print('A is:',A)
        else:
            continue
    return sum(A)


m = int(input())
print(get_change(m))
