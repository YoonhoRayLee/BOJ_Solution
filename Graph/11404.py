#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.11404

import sys

n = int(input())
m = int(input())
costs = [[sys.maxsize]*(n+1) for i in range(n+1)]

for i in range(m):
    x, y, cost = map(int, sys.stdin.readline().strip().split())
    if cost < costs[x][y]:
        costs[x][y] = cost

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if x != y and costs[i][j] > costs[i][k]+costs[k][j]:
                costs[i][j] = costs[i][k]+costs[k][j]
            elif i==j:
                costs[i][j] = 0

for row in costs[1:]:
    for col in row[1:]:
        if col == sys.maxsize:
            print(0, end=" ")
        else:
            print(col, end=" ")
    print()