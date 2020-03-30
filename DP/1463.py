import sys

input = int(input())
dp= []
dp.append(0)
dp.append(0)
dp.append(1)

for i in range(3, input+1):
    temp = dp[i-1] + 1
    dp.append(temp)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1) 
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[input])