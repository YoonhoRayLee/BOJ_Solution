#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2884

H, M = map(int, input().split())

newM = M - 45 
newH = H - 1

if M - 45 < 0:
    M = 60 + newM
    if H - 1 < 0:
        H = 24 + newH
    else:
        H = newH
    print(H, M)
else:
    M = newM
    print(H, M)
