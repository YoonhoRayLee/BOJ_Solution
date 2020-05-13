#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2293

import sys
 
n, k = list(map(int, sys.stdin.readline().split()))
coins = []
for i in range(n):
    temp = int(sys.stdin.readline())
    coins.append(temp)
 
dp = [0 for i in range(10001)]
dp[0] = 1
for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
 
print(dp[k])