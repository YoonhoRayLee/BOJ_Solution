#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.9461

import sys

T = int(input())
N = []
for i in range(T):
    N.append(int(input()))
dp = []
dp.append(0)
dp.append(1)
dp.append(1)
dp.append(1)
maxN = max(N)

for i in range(T):
    for j in range(4, maxN+1):
        dp.append(dp[j-3]+dp[j-2])

for i in range(T):
    print(dp[N[i]])