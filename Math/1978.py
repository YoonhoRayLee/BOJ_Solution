#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1978

N = int(input())
arr = list(map(int,input().split()))
cnt = 0

for i in range(N):
    if arr[i] == 1:
        continue
    else:
        tempCnt = 0
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                tempCnt = tempCnt + 1
        if tempCnt == 0:
            cnt = cnt+1
            
print(cnt)