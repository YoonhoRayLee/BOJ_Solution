#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2798

N, M = map(int, input().split())
arr = list(map(int, input().split()))

maxNum = -9999

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = arr[i]+arr[j]+arr[k]
            if temp >= maxNum and temp<=M:
                maxNum = temp

print(maxNum)