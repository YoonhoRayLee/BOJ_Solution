#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2577

A = int(input())
B = int(input())
C = int(input())

mul = A*B*C

ans = list(str(mul))

for i in range(10):
    print(ans.count(str(i)))
