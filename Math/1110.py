#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1110

def cycle(num):
    tNum = int(num/10)
    oNum = int(num%10)
    newNum = (tNum + oNum)%10
    
    return (oNum*10 + newNum)

num = int(input())
firstNum = num

if num < 0 or num >99:
    exit()
else:
    cnt = 0
    while(1):
        if firstNum == cycle(num):
            print(cnt+1)
            break
        else:
            num = cycle(num)
            cnt = cnt + 1