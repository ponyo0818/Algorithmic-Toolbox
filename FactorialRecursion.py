# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:40:38 2018

@author: FY
"""

def recur_factorial(n):
    #Function to return the factorial of a number using recursion
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
    

num=int(input("Enter the number: "))
print("The factorial of", num, "is", recur_factorial(num))