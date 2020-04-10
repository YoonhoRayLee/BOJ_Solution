#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.9461

N = int(input())
T = []
T.append(0)
P = []
P.append(0)
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0 for _ in range(N+1)]
# 0 0 0 0 0 0 0 0 0 0
if T[N] == 1:
    dp[N] = P[N]
for i in range(N-1,0,-1):
    curr = i + T[i] - 1
    # 기준 상담일 딱 맞을 떄 
    if curr == N:
        dp[i] = max(P[i], dp[i+1])
    # 기준 상담일 넘어가면
    elif curr > N:
        dp[i] = dp[i+1]
    # 기준 상담일 전이라면
    elif curr < N:
        dp[i] = max(P[i] + dp[curr + 1], dp[i+1])

print(dp[1])