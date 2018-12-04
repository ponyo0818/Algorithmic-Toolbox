# python 3

def fib(n):
    #added for demonstration purpose only
    global call_count
    call_count=call_count+1
    #end
    
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

call_count=0
for i in range(100):
    print(fib(i))
print(call_count)
    
