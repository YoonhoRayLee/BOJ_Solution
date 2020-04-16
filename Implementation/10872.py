#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.10872

N = int(input())

fac = 1
for i in range(1, N+1):
    fac *= i

print(fac)