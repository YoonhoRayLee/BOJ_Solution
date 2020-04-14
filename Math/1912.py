#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1912

import sys

n = int(input())
dp = []
arr = list(map(int, input().split()))

dp.append(arr[0])

for i in range(1,n):
    dp.append(max(dp[i-1]+arr[i-1], arr[i-1]))

print(max(dp))