import sys

n = int(input())

dp = [[0]*10 for i in range(0,n+1)]

dp[0] = [0,1,1,1,1,1,1,1,1,1]
dp[1] = [1,1,2,2,2,2,2,2,2,1]

for i in range(2,n):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
            
print(sum(dp[n-1])%1000000000)