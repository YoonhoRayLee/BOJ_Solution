#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11054

import sys
N = int(input())
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
dpInc = [0] * 1001
dpDec = [0] * 1001
resultDP = []
tempInc = []
tempDec = []
for i in range(1, N+1):
    dpDec[N-i+1]=1
    dpInc[i]=1
    for j in range(1,i):
        #증가 부분수열
        if A[i] > A[j] and dpInc[j]+1>dpInc[i]:
            dpInc[i] = dpInc[j]+1
        #감소 부분수열
        if A[N-i+1] > A[N-j+1] and dpDec[N-j+1]+1>dpDec[N-i+1]:
            dpDec[N-i+1] = dpDec[N-j+1]+1
for i in range(N):
    resultDP.append(dpDec[i]+dpInc[i])
print(max(resultDP)-1)