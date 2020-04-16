#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1037

N = int(input())
arr = list(map(int, input().split()))

min_num = 0
max_num = 0
for i in range(len(arr)):
    if i:
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]
    else:
        min_num = arr[i]
        max_num = arr[i]

print(min_num * max_num)