#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1699
import sys
N = int(input())
dp = []
dp.append(0)
for i in range(1, N+1):
    j = 1
    dp.append(sys.maxsize)
    while j**2 <= i:
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1 
        j += 1
print(dp[N])