#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11727

import sys

n = int(input())

dp=[]
dp.append(0)
dp.append(1)
dp.append(3)

for i in range(3,n+1):
    dp.append((dp[i-1] + 2*dp[i-2])%10007)

print(dp[n]%10007)