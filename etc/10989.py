#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1629
import sys
N = int(input())
series = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for num in range(len(series)):
    if series[num] !=0:
        for c in range(series[num]):
            print(num)