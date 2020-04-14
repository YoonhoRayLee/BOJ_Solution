#Dongguk University Computer Science Engineering
#Yoonho Ray Lee
#BOJ Solution for Problem.1475

import math
N = list(input())

list1 = []
list2 = []
count = 0

for i in N:
    if i == '6':
        count += 1
        continue
    if i == '9':
        count += 1
        continue
    if N.count(i) != 1:
        list1.append(i)

avg = int(math.ceil(count/2))

for i in list1:
    list2.append(list1.count(i))
list2.append(1)
list2.append(avg)

print(max(list2))
