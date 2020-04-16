#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.2490

sticks = ['D','C','B','A','E']

plays = []
for i in range(3):
    plays.append(list(map(int, input().split())))

for i in range(3):
    print(sticks[plays[i].count(1)])