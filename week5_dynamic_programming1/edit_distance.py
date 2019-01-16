# Uses python3

#operation to convert str1 to str2
def edit_distance(str1, str2,n,m):
    #write your code here

    #if string 2 is empty, the only option is to remove all characters of string 1
    if n==0:
        return m
    
    #likewise when string 1 is empty
    if m==0:
        return n
    #if last character of two strongs are same, nothing much to do
    #Ignore last string and get count for the remaining string
    if str1[n-1]==str2[m-1]:
        return edit_distance(str1,str2,n-1,m-1)
    
    #If last characters are not same,consider all three operations on last character
    #of first string, recursively compute minimum cost for all three operations and 
    #take minimum of three values
    return 1+min(edit_distance(str1,str2,n,m-1),    #Insert
                 edit_distance(str1,str2,n-1,m),    #Delete
                 edit_distance(str1,str2,m-1,n-1)   #Substitute
                 )
    

if __name__ == "__main__":
    str1=input()
    str2=input()
    print(edit_distance(str1,str2,len(str1),len(str2)))
