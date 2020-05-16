#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11051

import sys
N, K = list(map(int, sys.stdin.readline().strip().split()))
num = 1
den = 1
for i in range(K):
    num *= N-i
for j in range(1, K+1):
    den *= j
print((num//den)%10007)