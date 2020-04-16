#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.10871

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i])