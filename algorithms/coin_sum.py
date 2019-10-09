# Coin sum
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins
print(recMC([1,5,10,25],63))

def getWays(n, c):
    c.sort()
    arr = [0 for k in range(n + 1)]
    arr[0] = 1
    for coin in c:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    return arr[n]
print(10, [1, 2, 5])
