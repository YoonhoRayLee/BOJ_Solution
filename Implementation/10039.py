#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.10039

scores = []
for i in range(5):
    scores.append(int(input()))

sum = 0
for i in range(5):
    if scores[i] < 40:
        scores[i] = 40
    sum += scores[i]

print(sum//5)