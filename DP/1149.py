#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1149

import sys

N = int(input())

price = [[0]*3 for i in range(N)]

for i in range(N):
    tempList = list(map(int, input().split()))
    for j in range(3):
        price[i][j] = tempList[j]

dp = [[0]*3 for i in range(N+1)]
dp[1] = price[0]

for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1] + price[i-1][0], dp[i-1][2] + price[i-1][0])
    dp[i][1] = min(dp[i-1][0] + price[i-1][1], dp[i-1][2] + price[i-1][1])
    dp[i][2] = min(dp[i-1][0] + price[i-1][2], dp[i-1][1] + price[i-1][2])

print(min(dp[N]))
