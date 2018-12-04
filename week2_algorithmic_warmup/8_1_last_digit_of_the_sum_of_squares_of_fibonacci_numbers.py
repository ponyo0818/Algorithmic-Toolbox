# python3
## a code to find the last digit of the sum of square Fibonacci numbers 
## up to Fn
## https://www.sololearn.com/post/3848/?ref=app

import time

## a simple Fibonacci number genarator
def get_next_fib():
    previous, current = 0, 1
    yield previous
    yield current
    while True:
        previous, current = current, previous + current
        yield current

## find the Pisano sequence for any given number
## https://en.wikipedia.org/wiki/Pisano_period
"""
In number theory, the nth Pisano period, written π(n), 
is the period with which the sequence of Fibonacci numbers taken modulo n repeats
"""
def get_pisano_seq(m):
    def check(candidate):
        middle = len(candidate) // 2
        if middle == 0:
            return False
        for i in range(middle):
            if candidate[i] != candidate[middle + i]:
                return False
        return True
    seq = []
    for fib in get_next_fib():
        seq.append(fib % m)
        if (len(seq) % 2):
            if check(seq):
                return seq[:len(seq) // 2]

## get the last digits of the n-th and (n+1)-th Fib number 
## by using the Pisano sequence for 10 
def get_last_digits(n):
    seq = get_pisano_seq(10)
    return seq[n % len(seq)], seq[(n+1) % len(seq)]

## calculate the last digit of the sum of squared Fib numbers
## by using that F0^2+F1^2+.....+Fn^2 = Fn * F(n+1)
## https://math.stackexchange.com/questions/2469236/prove-that-sum-of-the-square-of-fibonacci-numbers-from-1-to-n-is-equal-to-the-nt
def fibonacci_sum_squares(n):
    previous, current = get_last_digits(n)
    return (previous * current) % 10
    
if __name__ == '__main__':
    try:
        n = int(input())
        #print(n)
    except ValueError as e:
        print('Enter a valid number')
        raise e 
    # n = 832564823476
    start_time = time.clock()
    result = fibonacci_sum_squares(n)
    end_time = time.clock()
    print (result)
   #print('The last digit of the sum of the squares of all Fibonacci numbers \nup to F{0} is {1}.'.format(n, result))
   #print('Calculated in {0} ms'.format((end_time-start_time)*1000))