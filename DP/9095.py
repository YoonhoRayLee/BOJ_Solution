import sys

T = int(input())

inputArr = []
dp = []
dp.append(0)
dp.append(1)
dp.append(2)
dp.append(4)
for i in range(T):
    inputArr.append(int(input()))

for j in range(4, max(inputArr)+1):
    dp.append(dp[j-3] + dp[j-2] + dp[j-1])

for i in range(T):
    print(dp[inputArr[i]])