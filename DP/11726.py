#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11726

import sys

n = int(input())
tile= [0]

if(n==0):
    print(n)
elif(1<=n<=2):
    for i in range(1,n+1):
        tile.append(n)
    result = tile[n] % 10007
    print(result)
else:
    tile = [0,1,2]
    for  i in range(3,n+1):
        tile.append(tile[i-2] + tile[i-1])
    result = tile[n] % 10007
    print(result)
