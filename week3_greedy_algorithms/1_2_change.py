# python3

def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         print ('i is:',i)
         numCoins = 1 + recMC(coinValueList,change-i)
         print('numCoins is: ',numCoins)
         if numCoins < minCoins:
            print('minCoins is:',minCoins)

            minCoins = numCoins
   return minCoins



m = int(input())
print(recMC([1,5,10],m))