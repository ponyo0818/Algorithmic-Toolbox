# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:45:25 2018

@author: FY
"""

#run loop from starting to length/2 and check first character to last character of string
#and second to second last one and so on


#Function to check string is palindrome or not

def isPalindrome(str):
    #Run loop from 0 to len/2
    for i in range(0,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True


#main function
s=str(input("type the string "))
ans=isPalindrome(s)

if ans==1:
    print("Yes")
else:
    print("No")
# =============================================================================
#     
# a="malayalam"
# print(int(len(a)/2))
# 
# =============================================================================
