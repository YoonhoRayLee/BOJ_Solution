#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1932

import sys

N = int(input())
dp = []
arrTri = []
for i in range(N):
    tempArr = list(map(int, sys.stdin.readline().strip().split()))
    arrTri.append(tempArr)

<<<<<<< HEAD
dp = arrTri
dp[1][0] += dp[0][0]
dp[1][1] += dp[0][0]
for i in range(2, N):
    for j in range (0, i+1):
        if j == 0 :
            dp[i][j] += dp[i-1][0]
        else:
            if(j==i) : 
                dp[i][j] += dp[i-1][j-1]
            else : 
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))
=======
dp.append(arrTri[0])
>>>>>>> eceae8e24e7fb834883ed1c75729b1b824410bee
