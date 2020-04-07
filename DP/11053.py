import sys

N = int(input())
A = list(map(int, input().split()))
max = 0
dp = []
#A  - - - - - -
#DP   - - - - - -
for i in range(0,N):
    cnt = 0
    for j in range(0,i):
        if A[j] < A[i]:
            if cnt < dp[j]:
                cnt = dp[j]
    dp.append(cnt + 1)
    if max < dp[i]:
        max = dp[i]

print(max)
