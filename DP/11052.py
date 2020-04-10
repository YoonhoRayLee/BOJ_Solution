#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11052

import sys

N = int(input())
arr = list(map(int, input().split()))
P = []
P.append(0)
for i in range(N):
    P.append(arr[i])
dp = []
dp.append(0)
dp.append(P[1])

for i in range(2,N+1):
    dp.append(P[i])
    for j in range(1,i):
        maxP = max((dp[i-j]+P[j]),P[i])
        if dp[i] < maxP:
            dp.insert(i,(max((dp[i-j]+P[j]), P[i])))

print(dp[N])