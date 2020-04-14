#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1712

A, B, C = map(int,input().split())

if B >= C:
    print(-1)
else:
    print((A//(C-B))+1)