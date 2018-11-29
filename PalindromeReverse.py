# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:40:31 2018

@author: FY
"""

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    #calling reverse function
    rev=reverse(s)
    
    #checking if both string are equal or not
    if(s==rev):
        return True
    return False

#Driver code

s=str(input("type the string "))
ans=isPalindrome(s)

if ans==1:
    print("Yes")
else:
    print("No")
    