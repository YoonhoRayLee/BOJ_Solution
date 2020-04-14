#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1010

import sys
from functools import reduce
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

T = int(input())
NM = []
NM.append(0)
for i in range(1, T+1):
    NM.append(list(map(int,input().split())))

for i in range(1, T+1):
    if NM[i][0] == 1:
        print(NM[i][1])
    elif NM[i][1] - NM[i][0] == 0:
        print(1)
    else:
        print(ncr(NM[i][1], NM[i][0]))