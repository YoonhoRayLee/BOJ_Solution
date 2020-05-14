#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11055

import sys
N = int(input())
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = []
dp.append(0)
for i in range(1, N+1):
    temp = []
    for j in range(i-1,-1, -1):
        if A[i] > A[j] :
            temp.append(dp[j])
    if not temp :
        dp.append(A[i])
    else :
        dp.append(max(temp) + A[i])
print(max(dp))