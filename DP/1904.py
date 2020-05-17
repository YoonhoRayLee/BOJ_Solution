#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1904

import sys
N = int(input())
dp = []
dp.append(0)
dp.append(1)
dp.append(2)
for i in range(3,N+1):
    dp.append((dp[i-2]%15746+dp[i-1]%15746)%15746)
print(dp[N]%15746)