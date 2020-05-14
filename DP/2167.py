#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2167
import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    arr[i] = [0] + list(map(int, sys.stdin.readline().strip().split()))
K = int(input())
sub = []
dp = [[0] * (M+1) for _ in range(N+1)]

dp[1][1] = arr[1][1]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]+arr[i][j] - dp[i-1][j-1]

ans = []
for a in range(K):
    i, j, x, y = map(int, sys.stdin.readline().strip().split())
    result = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    ans.append(result)
for item in ans :
    print(item)