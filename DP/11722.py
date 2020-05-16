#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11722

import sys
N = int(input())
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * 1001
for i in range(1, N+1):
    dp[i]=1
    for j in range(i-1, -1, -1):
        if A[i]<A[j] and dp[i]<=dp[j]:
            dp[i]=dp[j]+1
print(max(dp))