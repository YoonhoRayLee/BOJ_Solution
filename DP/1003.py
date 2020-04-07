#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1003

import sys
T = int(input())
inputArr = []

dpZero = []
dpZero.append(1)
dpZero.append(0)
dpOne = []
dpOne.append(0)
dpOne.append(1)

for i in range(T):
    temp = int(input())
    if temp >40:
        exit()
    inputArr.append(temp)

dp = [[0]*2 for i in range(T)]

for j in range(2, max(inputArr)+1):
    dpZero.append(dpZero[j-2]+dpZero[j-1])
    dpOne.append(dpOne[j-2]+dpOne[j-1])

for i in range(T):
    dp[i][0] = dpZero[inputArr[i]]
    dp[i][1] = dpOne[inputArr[i]]
    print('{0} {1}'.format(dp[i][0], dp[i][1]))
