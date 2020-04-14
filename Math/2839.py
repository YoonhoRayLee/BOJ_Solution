#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2839

N = int(input())
dp = []
dp.append(0)
dp.append(-1)
dp.append(-1)
dp.append(1)
dp.append(-1)
dp.append(1)
for i in range(6, N+2):
    if dp[i-5] != -1:
        dp.append(dp[i-5]+1)
    elif dp[i-3] != -1:
        dp.append(dp[i-3]+1)
    else:
        dp.append(-1)

print(dp[N])
