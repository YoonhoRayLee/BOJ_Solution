#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2133

import sys
N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
    if i % 2 == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = 3
    else:
        temp = 0
        for j in range(2, i-1):
            if j == i-2:
                temp += dp[j] * 3
            elif j % 2 == 0:
                temp += dp[j] * 2
        dp[i] = temp + 2
print(dp[N])