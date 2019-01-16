# Uses python3

#operation to convert str1 to str2
def edit_distance(str1, str2,m,n):
    #write your code here

   dp=[[0 for x in range(n+1)]for x in range(m+1)]
   
   for i in range(m+1):
       for j in range(n+1):
           
           #if string 1 is empty
           if i==0:
               dp[i][j]=j
           #if string 2 is empty
           elif j==0:
               dp[i][j]=i
               
           #if last character are same, ignore them
           elif str1[i-1]==str2[j-1]:
               dp[i][j]=dp[i-1][j-1]
           
           #consider all possibilities and find minimum
           else:
               dp[i][j]=1+min(dp[i][j-1],
                              dp[i-1][j],
                              dp[i-1][j-1])
   return dp[m][n]

if __name__ == "__main__":
    str1=input()
    str2=input()
    print(edit_distance(str1,str2,len(str1),len(str2)))
