#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2579

import sys

N = int(input())

dp = []
dp.append(0)
scores = []
scores.append(0)

for i in range(N):
    scores.append(int(input()))

dp.append(scores[1])
if N <= 1:
    print(dp[N])
    exit()

dp.append(scores[1]+scores[2])

for i in range(3, N+1):
    dp.append(max(dp[i-3]+ scores[i-1] + scores[i], dp[i-2]+scores[i]))

print(dp[N])
