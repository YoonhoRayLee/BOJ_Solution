#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11057

#column : last num
#row : possibles 

# 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# 55, 45, 36, 28, 21, 15, 10, 6, 3, 1

N = int(input())
dp = [[1]*10 for _ in range(N+1)]
for i in range(2, N+1):
    for j in range(8, -1, -1):
        dp[i][j] = (dp[i-1][j]%10007+dp[i][j+1]%10007)%10007
print(sum(dp[N])%10007)