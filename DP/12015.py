#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.12015

import sys
sys.setrecursionlimit(10**8)
def search(low,high,n):
    if low == high:
        return low
    elif low + 1 == high:
        return low if C[low] >= n else high
    
    mid = (low+high)//2
    if C[mid] == n:
        return mid
    elif C[mid] < n:
        return search(mid+1, high, n)
    else:
        return search(low, mid, n)

N = int(input())
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
C = [sys.maxsize]*(N+1)
C[0] = -sys.maxsize
C[1] = A[0]
tmp_longest = 1

for n in A:
    if C[tmp_longest] < n:
        tmp_longest += 1
        C[tmp_longest] = n
    else:
        next_loc = search(0, tmp_longest, n)
        C[next_loc] = n
print(tmp_longest-1)