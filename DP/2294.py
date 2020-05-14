#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2294
import sys
n, k = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (k+1)
coins = []
for i in range(n):
    coins.append(int(input()))
coins = list(set(coins))
for i in range(1, k+1):
    minVal = sys.maxsize
    for j in coins:
        if i >= j:
            minVal = min(minVal, dp[i-j]+1)
    dp[i] = minVal
print(dp[k] if dp[k] != sys.maxsize else -1)