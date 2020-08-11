import sys
N, K = list(map(int, sys.stdin.readline().strip().split()))
A = [0] * 1000000
AA = 0
for i in range(N):
    A[i] = int(input())
    AA += A[i]
l = 0
r = AA+1
while l+1 < r:
    m = (l+r)/2
    S = [0]*1000000
    P = [0]*1000000
    for i in range(N):
        if i>0:
            P[i]=P[i-1]-1
            S[i]=S[i-1]-A[i-1]
        else:
            P[i]=0
            S[i]=0
        while S[i] < m:
            S[i] += A[(i+P[i])%N]
            P[i] += 1
    B = 0
    for i in range(N):
        if AA-S[i]-S[(i+P[i])%N]>=m:
            B=1
    if B:
        l = m
    else:
        r = m
print(l)


