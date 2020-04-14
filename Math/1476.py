#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1476

E, S, M = map(int, input().split())
e=1 
s=1 
m=1
day = 1
while True:
    if e == E and s == S and m == M:
        break
    if e+1<=15:
        e += 1
    else:
        e = 1
    if s+1<=28:
        s += 1
    else:
        s = 1
    if m+1<=19:
        m += 1
    else:
        m = 1
    day += 1

print(day)