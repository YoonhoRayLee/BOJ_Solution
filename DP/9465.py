#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.9465

T = int(input())
N = []
N.append(0)
arr = []
arr.append([0])

for i in range(1, T+1):
    N.append(int(input()))
    for j in range(0,2):
        arr.append(list(map(int,input().split())))

for i in range(1,T+1):
    dp = [[0 for col in range(N[i])] for row in range(2)]
    dp[0][0] = arr[2*i-1][0]
    dp[1][0] = arr[2*i][0]
    dp[0][1] = dp[1][0] + arr[2*i-1][1]
    dp[1][1] = dp[0][0] + arr[2*i][1]
    for k in range(2, N[i]):
        dp[0][k] = max(dp[1][k-1], dp[1][k-2])+arr[2*i-1][k]
        dp[1][k] = max(dp[0][k-1], dp[0][k-2])+arr[2*i][k]

    print(max(dp[0][N[i]-1],dp[1][N[i]-1]))