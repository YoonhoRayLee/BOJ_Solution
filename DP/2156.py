import sys

n = int(input())

arr = []
arr.append(-1)
for i in range(0,n):
    arr.append(int(input()))

dp = []
dp.append(0)
dp.append(arr[1])
if n > 1:
    dp.append(arr[1]+arr[2])
if n > 2:
    dp.append(max(arr[1]+arr[3], arr[2]+arr[3], arr[1]+arr[2]))
for i in range(4,n+1):
    dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1]))

print(max(dp))